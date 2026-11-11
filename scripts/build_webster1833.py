#!/usr/bin/env python3
"""Build the source-locked, text-only Servants of the Way Webster 1833 Bible foundation.

Digital edition/provider provenance is retained only in technical JSON/markdown metadata,
not public reading pages. No external libraries, scanned pages, Strong's data or commentary.
"""

BOOKS = [('GEN', 'Genesis', 'genesis'), ('EXO', 'Exodus', 'exodus'), ('LEV', 'Leviticus', 'leviticus'), ('NUM', 'Numbers', 'numbers'), ('DEU', 'Deuteronomy', 'deuteronomy'), ('JOS', 'Joshua', 'joshua'), ('JDG', 'Judges', 'judges'), ('RUT', 'Ruth', 'ruth'), ('1SA', '1 Samuel', 'first-samuel'), ('2SA', '2 Samuel', 'second-samuel'), ('1KI', '1 Kings', 'first-kings'), ('2KI', '2 Kings', 'second-kings'), ('1CH', '1 Chronicles', 'first-chronicles'), ('2CH', '2 Chronicles', 'second-chronicles'), ('EZR', 'Ezra', 'ezra'), ('NEH', 'Nehemiah', 'nehemiah'), ('EST', 'Esther', 'esther'), ('JOB', 'Job', 'job'), ('PSA', 'Psalms', 'psalms'), ('PRO', 'Proverbs', 'proverbs'), ('ECC', 'Ecclesiastes', 'ecclesiastes'), ('SNG', 'Song of Solomon', 'song-of-solomon'), ('ISA', 'Isaiah', 'isaiah'), ('JER', 'Jeremiah', 'jeremiah'), ('LAM', 'Lamentations', 'lamentations'), ('EZK', 'Ezekiel', 'ezekiel'), ('DAN', 'Daniel', 'daniel'), ('HOS', 'Hosea', 'hosea'), ('JOL', 'Joel', 'joel'), ('AMO', 'Amos', 'amos'), ('OBA', 'Obadiah', 'obadiah'), ('JON', 'Jonah', 'jonah'), ('MIC', 'Micah', 'micah'), ('NAM', 'Nahum', 'nahum'), ('HAB', 'Habakkuk', 'habakkuk'), ('ZEP', 'Zephaniah', 'zephaniah'), ('HAG', 'Haggai', 'haggai'), ('ZEC', 'Zechariah', 'zechariah'), ('MAL', 'Malachi', 'malachi'), ('MAT', 'Matthew', 'matthew'), ('MRK', 'Mark', 'mark'), ('LUK', 'Luke', 'luke'), ('JHN', 'John', 'john'), ('ACT', 'Acts', 'acts'), ('ROM', 'Romans', 'romans'), ('1CO', '1 Corinthians', 'first-corinthians'), ('2CO', '2 Corinthians', 'second-corinthians'), ('GAL', 'Galatians', 'galatians'), ('EPH', 'Ephesians', 'ephesians'), ('PHP', 'Philippians', 'philippians'), ('COL', 'Colossians', 'colossians'), ('1TH', '1 Thessalonians', 'first-thessalonians'), ('2TH', '2 Thessalonians', 'second-thessalonians'), ('1TI', '1 Timothy', 'first-timothy'), ('2TI', '2 Timothy', 'second-timothy'), ('TIT', 'Titus', 'titus'), ('PHM', 'Philemon', 'philemon'), ('HEB', 'Hebrews', 'hebrews'), ('JAS', 'James', 'james'), ('1PE', '1 Peter', 'first-peter'), ('2PE', '2 Peter', 'second-peter'), ('1JN', '1 John', 'first-john'), ('2JN', '2 John', 'second-john'), ('3JN', '3 John', 'third-john'), ('JUD', 'Jude', 'jude'), ('REV', 'Revelation', 'revelation')]

CSS = "\n:root{font-family:Georgia,'Times New Roman',serif;color:#192b32;background:#f7f5ef}\n*{box-sizing:border-box}body{margin:0}header{background:#132f37;color:#fcf8ec;padding:20px max(20px,calc((100vw - 1080px)/2))}\nheader small{color:#c8d7d1;letter-spacing:.11em;font:600 11px Arial,sans-serif}\nheader h1{font-weight:normal;font-size:clamp(25px,4vw,38px);margin:6px 0}\nmain{max-width:1080px;margin:24px auto;padding:0 16px}\n.panel{background:#fff;border:1px solid #d4d9d6;box-shadow:0 2px 16px #0b28350a;border-radius:12px;min-width:0;overflow:hidden}\n.toolbar{padding:15px;border-bottom:1px solid #e4e6e2;display:flex;gap:9px;align-items:center;flex-wrap:wrap}\n.toolbar label{font:600 13px Arial,sans-serif;color:#304f58}\nselect,button{font:14px Arial,sans-serif;border:1px solid #a8b4b6;border-radius:6px;padding:9px;background:#fff;color:#173943;max-width:100%}\nbutton{background:#1c515a;color:#fff;border-color:#1c515a;cursor:pointer}\nbutton:disabled{opacity:.4;cursor:default}\nbutton:focus-visible,select:focus-visible,a:focus-visible,.verse:focus-visible{outline:3px solid #b48f47;outline-offset:2px}\n#title{margin:0 0 12px;font-size:clamp(24px,4vw,32px);font-weight:normal}\n#text{padding:18px clamp(14px,4vw,34px) 26px;font-size:clamp(18px,2vw,21px);line-height:1.8}\n.verse{display:inline;cursor:pointer;border-radius:4px;padding:2px 1px;outline-offset:0}\n.verse:focus{outline:2px solid #b48f47}\n.verse.selected{background:#eff4ed;box-shadow:0 0 0 2px #96b2a3}\n.vnum{font:600 12px Arial,sans-serif;color:#51767c;vertical-align:super;margin-right:3px}\n.verse.paragraph::before{content:'';display:block;height:.9em}\n.supplied{font-style:italic}\n.superscription{font:italic 15px/1.65 Georgia,serif;color:#557078;margin:8px 0 16px}\n#selection{padding:16px;background:#f7faf7;border-top:1px solid #dce6df;font:14px/1.6 Arial,sans-serif}\n#selection strong{color:#1d414a}\n#error{color:#9c3933;padding:0 16px;font:14px Arial,sans-serif}\n.tools-note{font:13px/1.6 Arial,sans-serif;color:#60777b;margin:4px 0 0}\n.about{margin:24px 0;font:14px/1.65 Arial,sans-serif;color:#2c5058}\n.about summary{cursor:pointer;font-weight:700}.about a,a{color:#1a5562}footer{max-width:1080px;margin:0 auto 32px;padding:0 16px;font:12px/1.6 Arial,sans-serif;color:#577078}\n.navrow{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:space-between}\n@media(max-width:620px){.toolbar{align-items:flex-end}.toolbar select{min-width:100px}header{padding:18px 16px}#text{line-height:1.75}}\n"

JS = "(()=>{\n'use strict';\nconst root=document.documentElement;\nconst code=root.dataset.book;\nconst dataBase='../../../data/webster1833/';\nconst $=id=>document.getElementById(id);\nlet book=null,chapter=null,selectedVerse=1,bookList=[];\nfunction setError(s){$('error').textContent=s||'';}\nfunction urlFor(ch,v){return '#'+code+'.'+ch+'.'+v;}\nfunction selectedFromLocation(){\n const hash=decodeURIComponent(location.hash.replace(/^#/,''));\n const match=hash.match(/^([A-Z0-9]{3})\\.(\\d+)\\.(\\d+)$/);\n if(match && match[1]===code)return [Number(match[2]),Number(match[3])];\n const q=new URLSearchParams(location.search);const ref=q.get('ref');\n const m=ref&&ref.match(/^([A-Z0-9]{3})\\.(\\d+)\\.(\\d+)$/);\n if(m && m[1]===code)return [Number(m[2]),Number(m[3])];\n return [1,1];\n}\nasync function json(path){let r=await fetch(path,{cache:'no-cache'});if(!r.ok)throw new Error('Unable to load '+path+' (HTTP '+r.status+')');return r.json();}\nfunction makeOption(value,label){const o=document.createElement('option');o.value=String(value);o.textContent=label;return o;}\nasync function init(){\n try{\n const [books,catalog]=await Promise.all([json(dataBase+'books.json'),json(dataBase+'catalog-'+root.dataset.slug+'.json')]);\n bookList=books.books;book=catalog;\n $('bookName').textContent=book.book_name;\n $('title').textContent=book.book_name;\n $('bookSelect').replaceChildren(...bookList.map(b=>makeOption(b.code,b.name)));\n $('bookSelect').value=code;\n $('chapterSelect').replaceChildren(...Array.from({length:book.chapter_count},(_,i)=>makeOption(i+1,'Chapter '+(i+1))));\n $('bookSelect').addEventListener('change',()=>{\n   const b=bookList.find(x=>x.code===$('bookSelect').value);\n   if(b)location.href='../../../books/'+b.slug+'/site/index.html#'+b.code+'.1.1';\n });\n $('chapterSelect').addEventListener('change',()=>load(Number($('chapterSelect').value),1));\n $('verseSelect').addEventListener('change',()=>select(Number($('verseSelect').value),true));\n $('prev').addEventListener('click',()=>load(Number($('chapterSelect').value)-1,1));\n $('next').addEventListener('click',()=>load(Number($('chapterSelect').value)+1,1));\n $('copy').addEventListener('click',()=>navigator.clipboard?.writeText(location.href));\n window.addEventListener('hashchange',()=>{const [ch,v]=selectedFromLocation(); if(ch!==chapter?.chapter)load(ch,v);else select(v,false);});\n const [ch,v]=selectedFromLocation();await load(ch,v);\n }catch(e){setError(e.message);}\n}\nasync function load(ch,v){\n if(!book){return;}\n if(ch<1||ch>book.chapter_count){setError('That chapter is outside this book.');return;}\n try{\n  setError(''); const path=dataBase+root.dataset.slug+'/chapters/'+String(ch).padStart(2,'0')+'.json';\n  const [data,heads]=await Promise.all([json(path),json(dataBase+root.dataset.slug+'/chapter-extras.json')]);\n  if(data.book_code!==code||data.edition_id!=='WEBSTER1833'||data.chapter!==ch)throw new Error('Chapter identity mismatch');\n  chapter=data;\n  $('chapterSelect').value=String(ch);\n  $('prev').disabled=ch<=1;$('next').disabled=ch>=book.chapter_count;\n  $('verseSelect').replaceChildren(...data.verses.map(x=>makeOption(x.verse,'Verse '+x.verse)));\n  $('title').textContent=book.book_name+' · Chapter '+ch;\n  const verses=document.createDocumentFragment();\n  const extra=heads.chapters[String(ch)];\n  if(extra?.superscriptions?.length){const p=document.createElement('p');p.className='superscription';p.textContent=extra.superscriptions.join(' ');verses.append(p);}\n  for(const vrow of data.verses){\n   const el=document.createElement('span');el.className='verse'+(vrow.paragraph_start?' paragraph':'');el.id=vrow.id;el.tabIndex=0;el.setAttribute('role','button');el.setAttribute('aria-label',book.book_name+' '+ch+':'+vrow.verse);\n   const num=document.createElement('span');num.className='vnum';num.textContent=String(vrow.verse);el.append(num);\n   for(const sp of vrow.spans){const n=document.createElement('span');if(sp.kind==='supplied')n.className='supplied';n.textContent=sp.text;el.append(n);}\n   el.append(document.createTextNode(' '));\n   el.addEventListener('click',()=>select(vrow.verse,true));\n   el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(vrow.verse,true);}});\n   verses.append(el);\n  }\n  $('text').replaceChildren(verses);\n  select(v,true);\n }catch(e){setError(e.message);$('text').textContent='';}\n}\nfunction select(n,updateHash){\n if(!chapter)return;\n let row=chapter.verses.find(v=>v.verse===n)||chapter.verses[0];\n if(!row)return;\n selectedVerse=row.verse;\n $('verseSelect').value=String(selectedVerse);\n $('selectionRef').textContent=book.book_name+' '+chapter.chapter+':'+selectedVerse;\n $('selectionId').textContent=row.id;\n document.querySelectorAll('.verse.selected').forEach(el=>el.classList.remove('selected'));\n const el=document.getElementById(row.id);if(el)el.classList.add('selected');\n if(updateHash && location.hash!==urlFor(chapter.chapter,selectedVerse)) history.replaceState(null,'',urlFor(chapter.chapter,selectedVerse));\n}\ninit();\n})();\n"

PAGE = '<!doctype html><html lang="en" data-book="{code}" data-slug="{slug}">\n<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Servants of the Way | Webster\'s Bible | {name}</title><link rel="stylesheet" href="../../../assets/webster1833/reader.css"></head>\n<body><header><small>SERVANTS OF THE WAY · BIBLE FOUNDATION</small><h1>Webster\'s Bible · 1833</h1><div><span id="bookName">{name}</span> · Scripture text</div></header>\n<main><section class="panel"><div class="toolbar"><label for="bookSelect">Book</label><select id="bookSelect" aria-label="Select Bible book"></select><label for="chapterSelect">Chapter</label><select id="chapterSelect"></select><label for="verseSelect">Verse</label><select id="verseSelect"></select><button id="prev">Previous chapter</button><button id="next">Next chapter</button></div>\n<h2 id="title" style="padding:12px 20px 0">{name}</h2><div id="text" aria-live="polite"><p>Loading chapter…</p></div><p id="error" role="alert"></p><div id="selection"><strong id="selectionRef">Select a verse</strong> <span>· Reference ID: <code id="selectionId"></code></span> <button id="copy">Copy verse link</button></div></section>\n<details class="about"><summary>About This Translation</summary><p><strong>Noah Webster\'s Bible (1833)</strong> presents the Scriptures in Webster\'s revision of the common English Bible. The reader covers the 66 books of the Protestant canon.</p>\n<p>Presented by the <strong>Servants of the Way Digital Library</strong>. Translator-supplied English words are italicized where marked by this edition.</p><p>Original-language analysis and historical commentary are maintained separately and are not part of this text-only reader.</p></details>\n</main><footer>Webster\'s Bible · 1833 | Servants of the Way Digital Library</footer>\n<script src="../../../assets/webster1833/reader.js" defer></script></body></html>\n'

INDEX = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Servants of the Way | Webster\'s Bible</title><style>body{font:18px/1.5 Georgia,serif;background:#f7f5ef;color:#192b32;max-width:1050px;margin:0 auto;padding:28px}h1{font-weight:normal}a{color:#1b555d}ul{columns:3;list-style:none;padding:0}li{break-inside:avoid;padding:4px 0}@media(max-width:640px){ul{columns:2}}</style></head><body><small>SERVANTS OF THE WAY · BIBLE FOUNDATION</small><h1>Webster\'s Bible · 1833</h1><p>Presented by the Servants of the Way Digital Library. Select a book to read by chapter and verse.</p><ul>{items}</ul><p>Webster\'s Bible · 1833 | Servants of the Way Digital Library</p></body></html>'


import argparse
import collections
import hashlib
import json
import re
import shutil
import zipfile
from datetime import date
from pathlib import Path

EDITION = 'WEBSTER1833'
SOURCE_FILE = 'engwebster_usfm.zip'
SOURCE_ID = 'engwebster'
SOURCE_URL = 'https://ebible.org/engwebster'
DOWNLOAD_URL = 'https://ebible.org/Scriptures/engwebster_usfm.zip'

USFM_LINE = re.compile(r'^\\([a-z0-9]+)(?:\s+|$)(.*)$')
ADD_TAG = re.compile(r'(\\add\*?)')
UNKNOWN_MARKER = re.compile(r'\\[A-Za-z+]+')


def sha(b):return hashlib.sha256(b).hexdigest()
def dumps(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'

def make_parser(text, code):
    chapters=collections.OrderedDict()
    curr_ch=None
    seen_ids=set()
    for ln,line in enumerate(text.splitlines(),1):
        line=line.strip()
        if not line: continue
        match=USFM_LINE.fullmatch(line)
        if not match: raise ValueError(f'{code} line {ln}: unknown USFM line {line[:80]}')
        tag, rest = match.groups()
        if tag=='c':
            ch=int(rest.strip())
            if ch in chapters:raise ValueError(f'{code} duplicate chapter {ch}')
            chapters[ch]=[]
            curr_ch=ch
        elif tag=='v':
            if curr_ch is None:raise ValueError('verse before chapter')
            m=re.fullmatch(r'(\d+)(?:\s+|$)(.*)', rest)
            if not m:raise ValueError(f'Unrecognized verse marker {code} line {ln}')
            v=int(m.group(1)); raw=m.group(2)
            if UNKNOWN_MARKER.search(ADD_TAG.sub('',raw)):
                raise ValueError(f'Unknown inline marker {code}.{curr_ch}.{v}')
            spans=[]; italic=False
            for piece in ADD_TAG.split(raw):
                if piece=='\\add':
                    if italic:raise ValueError(f'Nested supplied marker {code}.{curr_ch}.{v}')
                    italic=True
                    continue
                if piece=='\\add*':
                    if not italic:raise ValueError(f'Orphan supplied marker {code}.{curr_ch}.{v}')
                    italic=False
                    continue
                piece=re.sub(r'\s+',' ',piece)
                if not piece:continue
                # USFM \add boundaries can leave a space before comma or another punctuation mark.
                # Remove layout spacing before punctuation, but never change spelling or punctuation.
                if spans and re.match(r'^\s*[,;:.!?\)\]]',piece):
                    spans[-1]['text']=spans[-1]['text'].rstrip(' ')
                    piece=piece.lstrip(' ')
                if spans and spans[-1]['text'].endswith(' ') and piece.startswith(' '):piece=piece.lstrip(' ')
                if not piece:continue
                kind='supplied' if italic else 'text'
                if spans and spans[-1]['kind']==kind:spans[-1]['text']+=piece
                else:spans.append({'text':piece,'kind':kind})
            if italic:raise ValueError(f'Unclosed supplied marker at {code}.{curr_ch}.{v}')
            if not spans:raise ValueError(f'Blank verse at {code}.{curr_ch}.{v}')
            spans[0]['text']=spans[0]['text'].lstrip()
            spans[-1]['text']=spans[-1]['text'].rstrip()
            spans=[x for x in spans if x['text']]
            rid=f'{code}.{curr_ch}.{v}'
            if rid in seen_ids:raise ValueError(f'Duplicate verse {rid}')
            seen_ids.add(rid)
            chapters[curr_ch].append({'id':rid,'edition_verse_id':f'{EDITION}:{rid}',
                                      'verse':v,'spans':spans,'paragraph_start':v==1})
        elif tag in ('p','id','h','toc1','toc2','toc3','mt1','mt2'):
            if tag=='p' and rest:raise ValueError(f'Unexpected paragraph text {code} line {ln}')
        else:raise ValueError(f'Unsupported source marker {code} {tag} line {ln}')
    return chapters


def build(source, root, release_dir, date_str):
    root=Path(root);release_dir=Path(release_dir);source=Path(source)
    if root.exists():shutil.rmtree(root)
    if release_dir.exists():shutil.rmtree(release_dir)
    root.mkdir(parents=True);release_dir.mkdir(parents=True)
    def put(p,content):
        o=root/p;o.parent.mkdir(parents=True,exist_ok=True)
        o.write_bytes(content if isinstance(content,bytes) else content.encode('utf8'))
    def jput(p,obj):put(p,dumps(obj))
    archive_sha=sha(source.read_bytes())
    with zipfile.ZipFile(source,'r') as z:
        if z.testzip() is not None:raise ValueError('Damaged source ZIP')
        names=z.namelist(); usfm=[p for p in names if p.endswith('.usfm')]
        if len(usfm)!=66:raise ValueError(f'Expected 66 USFM files, found {len(usfm)}')
        sig=z.read('signature.txt.asc').decode('utf8')
        listed={filename:digest for digest,filename in re.findall(r'^([0-9a-f]{64})  ([^\r\n]+)$',sig,re.M)}
        if len(listed)!=68:raise ValueError(f'Source listed checksum count is {len(listed)}, expected 68')
        failures=[p for p,digest in listed.items() if p not in names or sha(z.read(p))!=digest]
        if failures:raise ValueError('Signed-list SHA-256 mismatches: '+', '.join(failures))
        source_map={re.fullmatch(r'\d+-([A-Z0-9]+)engwebster\.usfm',p).group(1):p for p in usfm}
        if set(source_map)!={t[0] for t in BOOKS}:raise ValueError('Book code mismatch')
        total_verses=total_chapters=total_supplied=0
        books_meta=[];origins=[]
        for i,(code,name,slug) in enumerate(BOOKS):
            filename=source_map[code]
            src=z.read(filename)
            content=src.decode('utf-8-sig')
            if not re.search(r'^\\id\s+'+re.escape(code)+r'\b',content,re.M):raise ValueError(f'ID mismatch in {code}')
            chaptermap=make_parser(content,code)
            if list(chaptermap)!=list(range(1,len(chaptermap)+1)):raise ValueError(f'Noncontiguous chapters {code}')
            book_verses=0;counts=[]
            for chapter,vs in chaptermap.items():
                if [v['verse'] for v in vs]!=list(range(1,len(vs)+1)):
                    raise ValueError(f'Noncontiguous verses {code}.{chapter}')
                if any(not v['spans'] or any(not x['text'] for x in v['spans']) for v in vs):raise ValueError('Empty spans')
                rel=f'data/webster1833/{slug}/chapters/{chapter:02d}.json'
                jput(rel,{'schema_version':'1.0.0','edition_id':EDITION,'book_code':code,'chapter':chapter,'verses':vs})
                b=(root/rel).read_bytes()
                if re.search(rb'\\(?:add|w|f)\b|strongs|"strong"',b,re.I):raise ValueError('Forbidden source annotation in '+rel)
                counts.append({'chapter':chapter,'verse_count':len(vs),'sha256':sha(b)})
                book_verses+=len(vs)
            chapters=len(chaptermap)
            total_chapters+=chapters;total_verses+=book_verses
            # A source occurrence \add...\add* becomes one italic span, occasionally merged when adjacent.
            add_count=len(re.findall(r'\\add(?=\s)',content));total_supplied+=add_count
            catalog={'schema_version':'1.0.0','edition_id':EDITION,'book_code':code,'book_name':name,'book_order':i+1,
                     'canonical_ids':f'{code}.{{chapter}}.{{verse}}','edition_ids':f'{EDITION}:{code}.{{chapter}}.{{verse}}',
                     'chapter_count':chapters,'verse_count':book_verses,'traditional_verse_positions':book_verses,
                     'omitted_from_main_text':[],'chapter_path_template':f'{slug}/chapters/{{chapter:02d}}.json',
                     'predecessor_book_code':BOOKS[i-1][0] if i else None,
                     'successor_book_code':BOOKS[i+1][0] if i<len(BOOKS)-1 else None,
                     'source_provenance':f'books/{slug}/SOURCE_INVENTORY.json','reader':f'books/{slug}/site/index.html',
                     'note':'Text-only Webster 1833 source projection. No scans, Strong’s markup, lexicons, or commentary.'}
            jput(f'data/webster1833/catalog-{slug}.json',catalog)
            # Same ASV/KJV integration paths; empty supplementary records are intentional.
            jput(f'data/webster1833/{slug}/chapter-extras.json',{'edition_id':EDITION,'book_code':code,'chapters':{},
                  'note':'No independent chapter-heading/superscription markers found. Source Psalm headings occurring inside verses remain in those numbered verses.'})
            jput(f'data/webster1833/{slug}/source-footnotes.json',{'edition_id':EDITION,'book_code':code,'chapters':{},
                  'note':'No USFM footnote markers in this source. No commentary or note text was added.'})
            jput(f'data/webster1833/{slug}/chapter-checks.json',{'edition_id':EDITION,'book_code':code,'chapter_count':chapters,'verse_count':book_verses,'chapters':counts})
            jput(f'books/{slug}/SOURCE_INVENTORY.json',{'edition_id':EDITION,'book_code':code,
                   'original_archive':SOURCE_FILE,'archive_sha256':archive_sha,'usfm_filename':filename,'usfm_sha256':sha(src),
                   'source_url':SOURCE_URL,'upstream_download':DOWNLOAD_URL,
                   'source_edition':'Noah Webster Bible, 1833; eBible engwebster USFM data',
                   'acquisition':'owner-provided vetted USFM archive; installed data derived from bytes of this archive',
                   'source_archive_preserved_outside_public_repository':True,
                   'source_usfm_contains_strongs_annotations':False,'published_chapter_json_contains_strongs':False,
                   'historical_scans_included':False,'rights_summary':'Public Domain per archived copr.htm'})
            jput(f'books/{slug}/VALIDATION_REPORT.json',{'status':'PASS_SOURCE_PROJECTION_CHECKS','source_archive_sha256':archive_sha,
                   'edition_id':EDITION,'book_code':code,'book_name':name,'chapter_count':chapters,'verse_count':book_verses,
                   'source_verse_markers':len(re.findall(r'^\\v\s+',content,re.M)),'source_supplied_word_runs':add_count,
                   'source_word_link_tags':0,'source_footnotes':0,'data_schema':'ASV/KJV-compatible v1.0.0 chapter records',
                   'limitations':'No independent character-for-character comparison to a first-print 1833 edition or GitHub Pages browser verification.'})
            put(f'books/{slug}/site/index.html',PAGE.format(code=code,slug=slug,name=name))
            put(f'books/{slug}/index.html',f'<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html#{code}.1.1"><title>Webster 1833 {name}</title><a href="site/index.html#{code}.1.1">Read {name}</a></html>\n')
            put(f'books/{slug}/README.md',f'''# {name} | Webster Bible (1833)

Servants of the Way Digital Library | Book {i+1} of 66.

{chapters} chapters, {book_verses:,} verses. Canonical identity `{code}.1.1`; edition identity `{EDITION}:{code}.1.1`.

The chapter JSON contains Scripture text and italicized supplied-word spans. No embedded Strong's, lexical notes, source scans, or commentary. Digital edition provenance is retained in `SOURCE_INVENTORY.json`; the source archive itself remains outside this translation repository.

The standalone reader is `books/{slug}/site/index.html`. Study resources remain separate and are not presented as built integrations.
''')
            books_meta.append({'code':code,'name':name,'slug':slug,'order':i+1,'chapter_count':chapters,'verse_count':book_verses,
                'verse_id_pattern':f'{code}.{{chapter}}.{{verse}}','edition_verse_id_pattern':f'{EDITION}:{code}.{{chapter}}.{{verse}}'})
            origins.append({'book_code':code,'source_file':filename,'sha256':sha(src),'chapter_count':chapters,'verse_count':book_verses})
        if (total_chapters,total_verses)!=(1189,31102):raise ValueError(f'Unexpected chapter/verse totals: {total_chapters}/{total_verses}')
        jput('data/webster1833/books.json',{'schema_version':'1.0.0','edition_id':EDITION,'title':"Webster's Bible (1833)",
            'book_count':66,'chapter_count':total_chapters,'verse_count':total_verses,'books':books_meta})
        jput('data/webster1833/route-map.json',{'schema_version':'1.0.0','edition_id':EDITION,
            'canonical_id_pattern':'{BOOK}.{CHAPTER}.{VERSE}',
            'edition_verse_id_pattern':'WEBSTER1833:{BOOK}.{CHAPTER}.{VERSE}',
            'book_catalog_path':'data/webster1833/catalog-{slug}.json',
            'chapter_text_path':'data/webster1833/{slug}/chapters/{chapter:02d}.json',
            'separate_original_language_resource':'SOTW-Original-Languages/original-language-resources and SOTW-Original-Languages-2/original-language-resources',
            'language_resource_route_map':'study-data/v1/route-map.json',
            'study_evidence_key_example':'verses["GEN.1.1"].WEBSTER1833',
            'note':'Edition-linked study data belongs to external original-language repositories. Logical future hook only; no English word offsets or links are asserted here.',
            'historical_commentary_resource':'SOTW-Historical-Commentaries/historical-commentary-resources',
            'commentary_join_id':'GEN.1.1','published_integration_status':'NOT_BUILT','facsimile_pages_available':False})
        jput('docs/SOURCE_LOCK.json',{'source_archive':SOURCE_FILE,'archive_sha256':archive_sha,
           'source_page':SOURCE_URL,'upstream_download':DOWNLOAD_URL,'source_title':'Noah Webster Bible',
           'source_id':SOURCE_ID,'source_description':'Noah Webster 1833 revision of common English Bible, USFM edition',
           'source_generated_at_in_archived_copyright_page':'2026-10-30',
           'source_signed_manifest':'signature.txt.asc','signed_sha256_entry_count':len(listed),
           'signed_manifest_hash_verification':f'{len(listed)}_OF_{len(listed)}_MATCH',
           'signed_manifest_signature_cryptographically_verified':False,
           'source_files':origins,'rights':'Public Domain per source copr.htm. Digital source attribution is stored as metadata only, not displayed in reader.'})
        jput('docs/EDITION.json',{'schema_version':'1.0.0','edition_id':EDITION,
           'translation_title':"Noah Webster's Bible",'first_publication_year':1833,'digital_source_id':SOURCE_ID,
           'digital_format':'USFM','canon':'Protestant 66 books','source_url':SOURCE_URL,
           'source_archive_sha256':archive_sha,'presenting_library':'Servants of the Way Digital Library',
           'public_display_label':"Webster's Bible · 1833",'rights_summary':'Public Domain per eBible source copr.htm',
           'capabilities':{'verses':True,'chapter_navigation':True,'book_navigation':True,'supplied_word_italics':True,
             'source_note_archival':True,'source_pdf_scan':False,'embedded_strongs':False,
             'original_language_word_click_ui':False,'historical_commentary_ui':False}})
        put('docs/RIGHTS_AND_PROVENANCE.md',f'''# Webster 1833 | rights and provenance record

Technical documentation. This material is **not** presented in the public Scripture reader.

- Source archive: `{SOURCE_FILE}`; provided by owner as vetted translation text
- Source URL: {SOURCE_URL}
- Original archive SHA-256: `{archive_sha}`
- Source copy rights statement: `copr.htm` calls it "Public Domain" and names Noah Webster as translator
- Source conversion status: web-generated USFM, no 1833 original scan supplied
- Source checksum list: 68 entries, all 68 SHA-256 digests independently checked against archive bytes
- The checksum list appears inside an OpenPGP-signed message, but its cryptographic signature has **not** been separately authenticated
- All 66 source-file hashes: `docs/SOURCE_LOCK.json`; book-specific paths: `books/<slug>/SOURCE_INVENTORY.json`
- This repository publishes only English Bible chapter data, plus reader/identity/technical documentation
- Original source ZIP remains outside the publicly distributed repository. No source USFM or dictionary content is bundled
- No source/provider promotional links appear in the website viewer; citations remain in metadata for reproducibility and rights
- No claim of facsimile collated 1833 first printing or independently verified lexical word alignments
''')
        put('docs/COMPATIBILITY.md', '''# Stable Scripture identity and cross-foundation compatibility

- `GEN.1.1` identifies a Scripture reference independently of its translation.
- `WEBSTER1833:GEN.1.1` identifies this Webster Bible verse's edition record.
- The English text appears only in `data/webster1833/{slug}/chapters/{NN}.json` using ASV/KJV-compatible `verses[]` and `spans[]`.
- Separate original-language repositories already index `WEBSTER1833` for accepted word-link evidence. That data is not Scripture text and is not imported here.
- An English verse reference is NOT proof of word-by-word correspondence across translations. Do not infer Strong's alignments, token offsets, or original-language meanings from the English spans.
- Historical-commentary passages can be joined by shared canonical references, but no API, commentary text, or UI integration is asserted as operational.
- The existing ASV, KJV, original-language repositories, and CGBC player remain unmodified by this standalone release.
''')
        put('docs/UPLOAD_GUIDE.md','''# Manual installation | Webster's Bible (1833)

## Target foundation

Recommended separate organization `SOTW-WEBSTER-1833` and repository `webster-1833-resources`. Use a **public**, initially empty repository. Use `main` as the default branch. Do not initialize a competing README, license, or .gitignore if uploading this source package verbatim.

## Install the numbered packs

1. Unzip the outer `SOTW_WEBSTER1833_MANUAL_UPLOAD_KIT_2026-11-10.zip`.
2. Extract `UPLOAD_PART_01_of_19.zip` into a folder; select **the files and folders inside it** (not the wrapper folder or ZIP) and use GitHub's repository root `Add file` / `Upload files` (or `uploading an existing file` on an empty repository).
3. Commit to `main` and repeat in sequence through Pack 19. Every package has at most 95 files; each file is under 25 MiB. The 19 packs have no duplicate repository-root file paths.
4. GitHub does **not** automatically unpack ZIP uploads. The extracted folder hierarchy must be preserved: `books/`, `data/`, `docs/`, `assets/`, `scripts/`, plus root files.
5. Verify all 1,797 repository files, 66 book catalogs, 1,189 chapter files and 31,102 verse records, using `RELEASE_MANIFEST.json` (SHA-256 values) and `UPLOAD_PLAN.json` (partition map).

## Publish the reader separately

After all packs have been installed, open repository `Settings → Pages` and choose `Deploy from a branch`, branch `main`, folder `/(root)`, then Save. Planned website: `https://sotw-webster-1833.github.io/webster-1833-resources/` if those exact names are used.

Test Genesis 1:1, Psalm 23, Matthew 1, Romans 10, and Revelation 22, chapter navigation, `#GEN.1.1`, `?ref=GEN.1.1`, and mobile display. No site deployment or external browser test is claimed by the archive.

Source provenance remains in the technical metadata. The public reader carries only Webster 1833 / Servants of the Way branding. No Strong's data or commentary is included.
''')
        put('docs/QA_REPORT.md',f'''# Webster1833 release audit | {date_str}

- **Source archive SHA-256:** `{archive_sha}`
- **Source contents:** 70 entries: 66 USFM book files, `copr.htm`, `dejavuserif.css`, `keys.asc`, and `signature.txt.asc`.
- **Listed SHA-256 entries:** {len(listed)}/{len(listed)} match source archive bytes; *OpenPGP signature verification not performed*.
- **Scope:** 66 books, {total_chapters:,} chapters and {total_verses:,} verse records, contiguous identifiers at book/chapter/verse level.
- **Source supplied-word markup:** {total_supplied:,} `\\add` starts preserved as italicized passage spans.
- **No source lexical markers:** 0 Strong's tags; no dictionary, lexical conclusions or historical-commentary text added.
- **Psalm introductory text:** retained where present *within* source numbered verses; no fabricated independent headings.
- **No source footnotes:** no `\\f` tags found; empty footnote metadata remains for structural compatibility.
- **Whitespace:** source's presentation-only trailing spaces normalized; spaces accidentally falling before punctuation after italic spans normalized without changing punctuation or spelling.
- **Provenance:** source archive and 66 per-book source SHA-256 hashes retained in metadata; source ZIP itself excluded from website ZIPs.
- **Limitations:** no independent character-by-character comparison with a historical 1833 printing; no deployed-site or browser acceptance claim.
- **Status:** Source-anchored structural conversion and hashes validated; GitHub Pages deployment awaits owner manual installation.
''')
        put('README.md',f'''# Servants of the Way Digital Library | Webster's Bible (1833)

Independent, text-only **Webster's Bible (1833)** translation foundation following the established ASV 1901 / KJV 1769 book, chapter, and verse data layout.

**Coverage:** 66 books, 1,189 chapters and 31,102 verses. Canonical IDs are shared (`GEN.1.1`); edition IDs are independent (`WEBSTER1833:GEN.1.1`).

- `index.html`: public Bible book selector.
- `books/<slug>/site/index.html`: book/chapter/verse readers.
- `data/webster1833/<slug>/chapters/NN.json`: English verse text, with printed supplied-word italics as `spans`.
- `data/webster1833/catalog-<slug>.json`: per-book metadata and navigation structure.
- `data/webster1833/route-map.json`: logical future cross-foundation reference hooks.
- `docs/EDITION.json` and `docs/SOURCE_LOCK.json`: digital source identity, rights, per-file provenance and SHA-256 locks (source data retained in metadata, **not displayed** in reader).
- `docs/UPLOAD_GUIDE.md`: owner installation and GitHub Pages setup.

Presented by the **Servants of the Way Digital Library**. No scans, embedded Strong's data, dictionary content or historical commentaries; future verse-click study information belongs to the existing independent foundations. This package does not alter any other repository or deploy a site.
''')
        put('assets/webster1833/reader.css',CSS)
        put('assets/webster1833/reader.js',JS)
        put('index.html',INDEX.replace('{items}',''.join(f'<li><a href="books/{slug}/site/index.html#{code}.1.1">{name}</a></li>' for code,name,slug in BOOKS)))
        # Keep the reproducible, standalone generator, parameterized by --source/--root/--release-dir.
        put('scripts/build_webster1833.py',Path(__file__).read_text(encoding='utf8'))
        files=sorted(str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*') if p.is_file())
        shas={name:sha((root/name).read_bytes()) for name in files}
        jput('RELEASE_MANIFEST.json',{'schema_version':'1.0.0','edition_id':EDITION,'release_date':date_str,
              'source_archive_sha256':archive_sha,'files':shas,'file_count_excluding_manifest':len(files),
              'sources_published_with_embedded_strongs':False,'release_type':'owner-manual-upload; NOT_DEPLOYED'})
        final_files=sorted(str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*') if p.is_file())
        if len(final_files)!=1797:raise ValueError(f'Wrong release file count: {len(final_files)}')
        cf=[n for n in final_files if re.fullmatch(r'data/webster1833/[^/]+/chapters/\d\d+\.json',n)]
        if len(cf)!=1189:raise ValueError('Chapter file count mismatch')
        if len([n for n in final_files if n.endswith('/site/index.html')])!=66:raise ValueError('Missing reader files')
        if any(f.endswith('.usfm') or f.endswith('.pdf') for f in final_files):raise ValueError('Source file leaked into publication')
        # Verify text and release hash manifest before partitioning.
        release_m=json.loads((root/'RELEASE_MANIFEST.json').read_text())
        for name,checksum in release_m['files'].items():
            if sha((root/name).read_bytes())!=checksum:raise ValueError('Release file checksum failed: '+name)
        for name in cf:
            ch=json.loads((root/name).read_text())
            if not ch['verses'] or len(ch['verses'])!=len(set(v['id'] for v in ch['verses'])):
                raise ValueError('Duplicate/missing verses: '+name)
        batch_count=(len(final_files)+94)//95
        if batch_count!=19:raise ValueError(f'Expected 19 packs, found {batch_count}')
        parts=[]
        for i in range(batch_count):
            batch=final_files[i*95:(i+1)*95]
            part=f'UPLOAD_PART_{i+1:02d}_of_{batch_count:02d}.zip'
            pp=release_dir/part
            with zipfile.ZipFile(pp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zpp:
                for name in batch:zpp.write(root/name,arcname=name)
            with zipfile.ZipFile(pp) as zpp:
                if zpp.testzip() is not None or len(zpp.namelist())>95:raise ValueError('Bad part')
            parts.append({'name':part,'file_count':len(batch),'bytes':pp.stat().st_size,'sha256':sha(pp.read_bytes()),'paths':batch})
        jplan={'edition_id':EDITION,'release_date':date_str,'repository_root_file_count':len(final_files),
               'zip_parts':len(parts),'upload_part_max_files':max(x['file_count'] for x in parts),
               'largest_individual_file_bytes':max((root/n).stat().st_size for n in final_files),
               'source_archive_sha256':archive_sha,'part_manifest':parts}
        (release_dir/'UPLOAD_PLAN.json').write_text(dumps(jplan))
        complete=release_dir/'SOTW_WEBSTER1833_COMPLETE_REPOSITORY_ROOT.zip'
        with zipfile.ZipFile(complete,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as full:
            for n in final_files:full.write(root/n,arcname=n)
        kit=release_dir.parent/'SOTW_WEBSTER1833_MANUAL_UPLOAD_KIT_2026-11-10.zip'
        with zipfile.ZipFile(kit,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as all:
            all.write(release_dir/'UPLOAD_PLAN.json',arcname='UPLOAD_PLAN.json')
            all.write(root/'docs/UPLOAD_GUIDE.md',arcname='UPLOAD_GUIDE.md')
            for p in parts:all.write(release_dir/p['name'],arcname=p['name'])
        with zipfile.ZipFile(kit) as zkit:
            if zkit.testzip() is not None:raise ValueError('Outer kit invalid')
        summary={'status':'BUILT_DATA_NOT_DEPLOYED','source_archive_sha256':archive_sha,
                'books':66,'chapters':total_chapters,'verses':total_verses,'source_supplied_word_runs':total_supplied,
                'release_file_count':len(final_files),'upload_part_count':len(parts),
                'part_counts':[p['file_count'] for p in parts],'max_file_bytes':jplan['largest_individual_file_bytes'],
                'complete_repository_zip':str(complete),'complete_bytes':complete.stat().st_size,
                'upload_kit':str(kit),'kit_bytes':kit.stat().st_size,'kit_sha256':sha(kit.read_bytes())}
        (release_dir/'SUMMARY.json').write_text(dumps(summary))
        print(dumps(summary))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Rebuild Webster's Bible (1833) public-domain translation foundation")
    parser.add_argument('--source',type=Path,default=Path('/mnt/data/engwebster_usfm.zip'))
    parser.add_argument('--root',type=Path,default=Path('/mnt/data/webster1833_work/SOTW_WEBSTER1833_REPOSITORY_ROOT'))
    parser.add_argument('--release-dir',type=Path,default=Path('/mnt/data/webster1833_work/release'))
    parser.add_argument('--date',default='2026-11-10')
    a=parser.parse_args()
    build(a.source,a.root,a.release_dir,a.date)
