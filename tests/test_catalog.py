import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build',ROOT/'scripts/build.py')
build=importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        shutil.copytree(ROOT/'catalog',self.root/'catalog')
        shutil.copytree(ROOT/'templates',self.root/'templates')

    def tearDown(self):
        self.tmp.cleanup()

    def read(self,rel):
        with (self.root/rel).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

    def write(self,rel,rows):
        with (self.root/rel).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=build.FIELDS,lineterminator='\n');w.writeheader();w.writerows(rows)

    def hashes(self):
        return {str(p.relative_to(self.root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (self.root/'catalog').rglob('*') if p.is_file()}

    def test_generator_is_deterministic_and_never_mutates_catalogs(self):
        before=self.hashes()
        first=build.generate(self.root)
        self.assertEqual(first,build.generate(self.root))
        self.assertEqual(before,self.hashes())

    def test_shared_paper_has_independent_metadata(self):
        a='catalog/methods/behavioral-imitation.csv';b='catalog/data/character-sources.csv'
        original_b=(self.root/b).read_bytes();rows=self.read(a)
        row=next(r for r in rows if r['id']=='wang2023rolellm')
        row['title']='Category-local amended title';row['venue']='Category-local venue'
        self.write(a,rows)
        result=build.generate(self.root)
        self.assertIn('Category-local amended title',result['literature/methods/behavioral-imitation.md'])
        self.assertNotIn('Category-local amended title',result['literature/data/character-sources.md'])
        self.assertEqual(original_b,(self.root/b).read_bytes())
        self.assertIn('Category-local amended title',result['literature/methods/behavioral-imitation.bib'])

    def test_new_paper_reaches_readme_and_exports(self):
        p='catalog/data/character-sources.csv';rows=self.read(p);new=dict(rows[0])
        new.update(id='test2026new',title='A newly added paper',doi='',arxiv_id='',paper_url='https://example.org/paper')
        rows.append(new);self.write(p,rows);out=build.generate(self.root)
        self.assertIn('A newly added paper',out['README.md'])
        self.assertIn('test2026new',out['exports/catalog.csv'])
        self.assertIn('test2026new',out['literature/data/character-sources.bib'])

    def test_duplicate_in_same_category_is_rejected(self):
        p='catalog/data/character-sources.csv';rows=self.read(p);rows.append(dict(rows[0]));self.write(p,rows)
        with self.assertRaisesRegex(ValueError,'duplicate id'):build.load(self.root)

    def test_unsafe_link_is_rejected(self):
        p='catalog/data/character-sources.csv';rows=self.read(p);rows[0]['paper_url']='javascript:alert(1)';self.write(p,rows)
        with self.assertRaisesRegex(ValueError,'invalid paper_url'):build.load(self.root)

    def test_title_cannot_inject_table_or_html(self):
        p='catalog/data/character-sources.csv';rows=self.read(p);rows[0]['title']='<script>x</script> | [fake](link)';self.write(p,rows)
        out=build.generate(self.root)['README.md']
        self.assertNotIn('<script>x</script>',out)
        self.assertIn(r'\| \[fake\]',out)

    def test_category_path_cannot_escape_repository(self):
        with self.assertRaisesRegex(ValueError,'escapes repository'):build.safe_path(self.root,'../outside.csv')

    def test_export_preserves_cross_category_occurrences(self):
        import io
        out=build.generate(self.root)
        rows=list(csv.DictReader(io.StringIO(out['exports/catalog.csv'])))
        matches=[r for r in rows if r['id']=='wang2023rolellm']
        self.assertGreater(len(matches),1)
        self.assertEqual(len(matches),len({r['category'] for r in matches}))
        stats=json.loads(out['exports/stats.json'])
        self.assertEqual(len(rows),stats['category_records'])


if __name__=='__main__':unittest.main()
