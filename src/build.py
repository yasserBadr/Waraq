from pathlib import Path
import base64, io, re, zipfile, json, hashlib

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'dist'
APP=OUT
APP.mkdir(parents=True, exist_ok=True)

chapters = [
('وقت للقراءة', [
'قد تبدأ الحكاية بدقائق قليلة. تفتح كتابًا، وتضع الهاتف جانبًا، وتترك للكلمات فرصة أن تصل إليك. لا تحتاج القراءة دائمًا إلى خطة كبيرة؛ تحتاج أحيانًا إلى مقعد مريح وصفحة واحدة.',
'في هذا الكتاب القصير، نجرّب أن نقرأ على مهل. انتقل بين الفصول من الفهرس، أو استخدم زر «التالي» أسفل الصفحة. تستطيع تغيير حجم الخط ولون الصفحة من إعدادات القراءة.',
'خذ نفسًا، ثم اقرأ الجملة مرة أخرى. ما الذي لفت انتباهك؟ لعل فكرة صغيرة تستحق أن تتوقف عندها. أضف إشارة مرجعية من الزر أعلى النافذة، لتعود إلى هذه الصفحة متى شئت.',
'حين تقرأ عشر صفحات بانتباه، قد تخرج منها بما يفوق ما تمنحك إياه عشرات الصفحات على عجل. ليست السرعة هي الغاية. الغاية أن تصغي للنص، وأن تترك له مساحة في يومك.',
'القراءة عادة هادئة، تنمو بالتكرار. اختر وقتًا قصيرًا يمكنك العودة إليه، ولا تجعل البداية أصعب من اللازم. خمس دقائق اليوم بداية كافية.',
'ضع علامة عند الجملة التي تود الاحتفاظ بها. وقد تجد في العودة إليها بعد أيام معنى لم تلاحظه أول مرة. تتغير قراءتنا لأن خبراتنا تتغير، وتبقى الكتب مفتوحة على أسئلة جديدة.',
'إذا ضاقت الصفحة، كبّر الخط. وإذا أتعبك الضوء، اختر الوضع الليلي. الكتاب الجيد يستحق أن تكون طريقته في الوصول إليك مريحة وواضحة.',
'جرّب البحث عن كلمة «القراءة» في لوحة البحث. ستظهر نتائج من الفصول المختلفة، ويمكنك الضغط على أي نتيجة للانتقال إلى موضعها.'
]),
('ما بين السطور', [
'لا يقدّم كل كتاب إجابات جاهزة. بعض الكتب تمنحنا سؤالًا أفضل، وبعضها يضع تجربة بعيدة أمامنا حتى نراها من زاوية جديدة. وقد تبقى معنا فقرة واحدة بعد أن ننسى بقية الصفحات.',
'اسأل نفسك وأنت تقرأ: ما الفكرة هنا؟ وما الذي يدعمها؟ وهل أوافق عليها لأنني فكرت فيها، أم لأنها تشبه ما كنت أعرفه من قبل؟ هذه الأسئلة لا تقطع متعة القراءة؛ قد تزيدها عمقًا.',
'للكلمات إيقاع أيضًا. جملة قصيرة تفتح نافذة، وأخرى طويلة تمشي بك في طريق متعرج. اقرأ أحيانًا بصوت خافت، ولاحظ كيف يتغير إحساسك بالنص.',
'قد نحتاج إلى التوقف عند مثال بسيط أكثر مما نحتاج إلى تجاوز فصل كامل. تخيّل الفكرة في موقف تعرفه، ثم اختبر حدودها: متى تصلح؟ ومتى تحتاج إلى تعديل؟',
'في القراءة مساحة للاختلاف. تستطيع أن تحترم الكاتب وأن تخالفه في الرأي، وأن تحب الكتاب دون أن تتفق مع كل ما فيه. احتفظ بأسئلتك كما تحتفظ بإشاراتك المرجعية.',
'هذه صفحة لاختبار النص المختلط أيضًا: يدعم القارئ EPUB 3، ويمكن تكبير الخط بنسبة 25% أو اختيار خط بسيط. الأسماء الإنجليزية تبقى في ترتيبها الطبيعي.',
'عند نهاية الفصل، اكتب في ذهنك جملة واحدة تلخّص ما فهمته. إن وجدت ذلك صعبًا، عد إلى الفقرة الأوضح، وابنِ منها الفكرة خطوة خطوة.'
]),
('العودة إلى الكتاب', [
'حين تعود إلى كتاب قرأته من قبل، لا تعود إلى المكان نفسه تمامًا. ربما تعرف اليوم ما لم تعرفه أمس، وربما ترى في الهامش سؤالًا لم يكن حاضرًا في قراءتك الأولى.',
'يحفظ ورق موضعك في هذا المتصفح. افتح الكتاب نفسه مرة أخرى لتتابع من حيث توقفت. ويمكنه الاحتفاظ بآخر كتاب محليًا إذا تركت خيار المتابعة مفعّلًا في الإعدادات.',
'إذا انتقلت إلى جهاز آخر، صدّر بيانات القراءة واحفظ ملف البيانات مع كتبك. ثم افتح القارئ هناك، واستورد البيانات، وافتح كتابك. ملف البيانات يحمل المواضع والإشارات، ولا يحمل نصوص الكتب.',
'جرّب الإعدادات حتى تجد ما يناسبك. لا يوجد حجم خط واحد يصلح للجميع، ولا وقت مثالي لا يتغير. اجعل القراءة عادة تلائم حياتك، واترك لها أن تتسع بهدوء.',
'هذا الكتاب نص تجريبي أصلي أُعدّ خصيصًا لاختبار القارئ. يمكنك استخدامه بحرية. والآن، اختر كتابًا من جهازك، وابدأ رحلتك الخاصة.',
'قد تنتهي الصفحات، وتبقى الفكرة. أغلق الكتاب حين تحتاج إلى ذلك، وارجع إليه حين تجد وقتًا. القراءة باب يمكنك فتحه من جديد.'
])]

def make_epub(epub2=False, english=False, malicious=False):
    lang='en' if english else 'ar'
    title='A quiet page' if english else 'على مهل'
    chs=[('First chapter',['A quiet page begins with a moment of attention. Reading opens another window. '*35,
         'A picture appears below. Search for the word window. '*25]),
         ('Second chapter',['The second chapter is a new beginning. Reading continues one page at a time. '*50])]
    if not english: chs=chapters
    stream=io.BytesIO()
    with zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('mimetype','application/epub+zip',compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml','<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        manifest=''.join(f'<item id="c{i}" href="chapter{i}.xhtml" media-type="application/xhtml+xml"/>' for i in range(len(chs)))
        items=''.join(f'<itemref idref="c{i}"/>' for i in range(len(chs)))
        z.writestr('EPUB/package.opf',f'''<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="{'2.0' if epub2 else '3.0'}" unique-identifier="uid"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uid">urn:waraq:demo:{lang}:{epub2}:{malicious}</dc:identifier><dc:title>{title}</dc:title><dc:creator>ورق</dc:creator><dc:language>{lang}</dc:language><meta property="dcterms:modified">2026-10-29T00:00:00Z</meta></metadata><manifest>{manifest}<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/><item id="style" href="style.css" media-type="text/css"/><item id="picture" href="picture.svg" media-type="image/svg+xml"/></manifest><spine toc="ncx" page-progression-direction="{'ltr' if english else 'rtl'}">{items}</spine></package>''')
        links=''.join(f'<li><a href="chapter{i}.xhtml">{t}</a></li>' for i,(t,_) in enumerate(chs))
        z.writestr('EPUB/nav.xhtml',f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}" dir="{"ltr" if english else "rtl"}"><head><title>الفهرس</title></head><body><nav epub:type="toc"><h1>الفهرس</h1><ol>{links}</ol></nav></body></html>')
        navs=''.join(f'<navPoint id="n{i}" playOrder="{i+1}"><navLabel><text>{t}</text></navLabel><content src="chapter{i}.xhtml"/></navPoint>' for i,(t,_) in enumerate(chs))
        z.writestr('EPUB/toc.ncx',f'<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="demo"/></head><docTitle><text>{title}</text></docTitle><navMap>{navs}</navMap></ncx>')
        z.writestr('EPUB/style.css','body{font-family:Georgia,Tahoma,serif;line-height:1.8;margin:0;padding:0 12px;} h1{font-size:1.75em;line-height:1.6;margin:0 0 1.2em;font-weight:normal;}p{margin:0 0 1em;text-align:start;}img{display:block;max-width:75%;margin:20px auto;}')
        z.writestr('EPUB/picture.svg','<svg xmlns="http://www.w3.org/2000/svg" width="320" height="100" viewBox="0 0 320 100"><rect width="320" height="100" rx="8" fill="#e8f0f8"/><path d="M115 24h90v53h-90z" fill="#315f8b"/><path d="M155 24h8v53h-8z" fill="#d2ac45"/></svg>')
        for i,(t,ps) in enumerate(chs):
            body=''.join(f'<p>{p}</p>' for p in ps)
            if english and i==0:body='<p><a href="chapter1.xhtml#target">Continue to second chapter</a></p>'+body
            if english and i==1:body='<p id="target">Internal link destination.</p>'+body
            if i==0:body+='<img src="picture.svg" alt="رسم لكتاب أزرق"/>'
            if malicious:body+='<script>parent.document.body.dataset.compromised="yes";</script><img src="https://example.com/tracker.png" onerror="parent.document.body.dataset.compromised=\'yes\'"/><a href="javascript:alert(1)">Bad link</a><iframe src="https://example.com"/><form><input value="unsafe"/></form>'
            z.writestr(f'EPUB/chapter{i}.xhtml',f'<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml" lang="{lang}" dir="{"ltr" if english else "rtl"}"><head><title>{t}</title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><h1>{t}</h1>{body}</body></html>')
    return stream.getvalue()

FIXTURES=ROOT.parent/'work'
FIXTURES.mkdir(exist_ok=True)
for name in ['README.txt','TESTED.txt']:
    (APP/name).write_bytes((ROOT.parent/'docs'/name).read_bytes())

demo=make_epub()
(APP/'Sample-Arabic.epub').write_bytes(demo)
vendors=[]
for name in ['jszip.min.js','epub.min.js']:
    text=(ROOT/'vendor'/name).read_text(encoding='utf-8-sig')
    text=re.sub(r'//# sourceMappingURL=.*','',text)
    text=text.replace('</script','<\\/script')
    vendors.append('<script>\n'+text+'\n</script>')
html=(ROOT/'index.html').read_text(encoding='utf-8')
epub_license=(ROOT/'vendor/EPUBJS-LICENSE.txt').read_text(encoding='utf-8-sig')
jszip_license=(ROOT/'vendor/JSZIP-LICENSE.txt').read_text(encoding='utf-8-sig').split('GPL version 3')[0]
license_comment='<!-- Bundled third-party licenses\nEPUB.js 0.3.93\n'+epub_license+'\nJSZip 3.10.1 (MIT option)\n'+jszip_license+'\n-->'
html=html.replace('<!-- VENDOR_JS -->',license_comment+'\n'+'\n'.join(vendors)).replace('__DEMO_EPUB__',base64.b64encode(demo).decode())
(APP/'Waraq.html').write_text(html,encoding='utf-8')
(APP/'Open-Waraq.cmd').write_bytes(b'@echo off\r\nstart "" "%~dp0Waraq.html"\r\n')
licenses='EPUB.js 0.3.93\nhttps://github.com/futurepress/epub.js\n\n'+(ROOT/'vendor/EPUBJS-LICENSE.txt').read_text(encoding='utf-8-sig')+'\n\nJSZip 3.10.1\nhttps://github.com/Stuk/jszip\nDistributed under the MIT option of its dual license.\n\n'+(ROOT/'vendor/JSZIP-LICENSE.txt').read_text(encoding='utf-8-sig')
(APP/'THIRD-PARTY-LICENSES.txt').write_text(licenses,encoding='utf-8')
(FIXTURES/'fixture-en-epub2.epub').write_bytes(make_epub(epub2=True,english=True))
(FIXTURES/'fixture-unsafe.epub').write_bytes(make_epub(english=True,malicious=True))
(FIXTURES/'invalid.epub').write_bytes(b'not an epub')
with zipfile.ZipFile(FIXTURES/'no-container.epub','w') as z:z.writestr('mimetype','application/epub+zip')
print(json.dumps({'html_bytes':len(html.encode()),'demo_bytes':len(demo),'output':str(APP)},ensure_ascii=False))
