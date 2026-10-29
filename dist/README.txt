Waraq 1.3 — Portable EPUB Reader
================================

Waraq is a lightweight EPUB reader that runs entirely in your browser from a
single HTML file. It needs no installation, no server, and no internet
connection.

Getting started
---------------
1. Extract the ZIP archive to any folder, including a USB drive.
2. Open Waraq.html in Microsoft Edge or Google Chrome.
   On Windows, you can also run Open-Waraq.cmd.
3. Choose an EPUB, or drag a book into the window.
4. For a quick trial, click the demo button inside the reader.

Keep THIRD-PARTY-LICENSES.txt with the package when you redistribute it.

What is included
----------------
- Waraq.html: the complete reader (HTML, CSS, JavaScript, and libraries).
- Sample-Arabic.epub: a short original Arabic demo book.
- Open-Waraq.cmd: Windows helper that opens the reader in the default browser.
- README.txt: this guide.
- TESTED.txt: verification summary and its limits.
- THIRD-PARTY-LICENSES.txt: licenses for EPUB.js and JSZip.

Features
--------
- EPUB 2 and EPUB 3 through EPUB.js.
- Arabic-first interface with RTL and LTR book support.
- Scroll reading (default), A4 portrait pages, and screen-sized pages.
- Chapter table of contents, full-text search, bookmarks, and resume.
- Light, sepia, and dark themes; adjustable font size, family, and line height.
- Focus mode, fullscreen, drag and drop, and keyboard shortcuts.
- Last-book cache (optional) for continuing without picking the file again.
- Export and import reading data as JSON to move positions between devices.
- No accounts, analytics, or book uploads.

Saving and moving
-----------------
The application is portable, but reading data is stored by the browser on each
device; it is never written into the HTML file or onto the USB drive. Before
changing browsers, devices, or the file location, export your reading data from
Settings. On the other device, open the reader, import the JSON file, then open
the same EPUB files. The JSON file does not contain the books.

Clearing browser data removes positions and the cached book. In private
browsing, storage is temporary, and some browsers restrict storage for local
file:// pages.

Keyboard shortcuts
------------------
Right / Left arrows: next / previous chapter in scroll mode, or next / previous
page in A4 and screen modes. The direction follows the book's reading direction.
Space or PageDown: scroll down. PageUp: scroll up.
Home / End: start / end of the chapter in scroll mode.
In A4 and screen modes, Space and PageDown turn to the next page.
B: add or remove a bookmark. /: search. F: focus mode. Esc: exit focus mode.
F11: browser fullscreen.
Shortcuts are ignored while typing in an input or while a dialog is open.

Limits
------
- Unprotected EPUB only. Waraq does not remove DRM and does not read PDF or MOBI.
- Maximum book file: 100 MB. Maximum uncompressed content: 400 MB.
- Progress is approximate, based on the spine and displayed pages, not printed
  page numbers.
- Search is plain text and shows the first 80 results. Arabic diacritics are
  not normalized automatically.
- Fixed-layout books, custom fonts, and encrypted resources may render
  differently. Changing the font size does not reflow fixed pages.
- Arabic fonts depend on the fonts installed on the device (for example Tahoma).
- Scripts and external resources inside books are disabled, so images that
  depend on remote URLs may not appear.

Privacy
-------
Waraq makes no network requests at runtime. The Content Security Policy blocks
remote content by default. Reading data stays in the browser's local storage;
the optional last-book cache uses IndexedDB. There are no analytics or upload
services.

Sample-Arabic.epub is an original demo book prepared for this project and may be
used freely. The editable source is src/index.html in the repository; the built
reader is dist/Waraq.html. Library licenses are in THIRD-PARTY-LICENSES.txt.

العربية
-------
ورق 1.3 — قارئ EPUB محمول

البدء
1. فك ضغط الحزمة في أي مجلد، أو على ذاكرة USB.
2. افتح Waraq.html باستخدام Microsoft Edge أو Google Chrome.
   ويمكن في Windows تشغيل Open-Waraq.cmd لفتح القارئ في المتصفح الافتراضي.
3. اضغط «اختر كتاب EPUB»، أو اسحب كتابك إلى النافذة.
4. للتجربة مباشرة، اضغط «جرّب كتابًا قصيرًا» داخل القارئ.

المزايا
- عرض EPUB 2 وEPUB 3 عبر EPUB.js.
- واجهة عربية واتجاه قراءة يدعم الكتب العربية والإنجليزية.
- قراءة بالتمرير، أو صفحات A4، أو صفحات بحجم مساحة القراءة.
- فهرس الفصول والبحث في النص والإشارات المرجعية واستعادة الموضع.
- أوضاع نهاري وورقي وليلي، وتحكم في الخط وحجمه وتباعده.
- وضع التركيز وملء الشاشة والسحب والإفلات واختصارات لوحة المفاتيح.
- الاحتفاظ بآخر كتاب في المتصفح للمتابعة، ويمكن تعطيل ذلك.
- تصدير واستيراد بيانات القراءة بصيغة JSON لنقل المواضع والإشارات.

الحفظ والنقل
التطبيق محمول، لكن بيانات القراءة تُحفظ في المتصفح على كل جهاز، ولا تُكتب داخل
ملف HTML أو على USB. عند تغيير المكان أو المتصفح أو الجهاز، صدّر بيانات القراءة
أولًا من الإعدادات، ثم استوردها في الجهاز الآخر وافتح ملفات EPUB نفسها. ملف
البيانات لا يحمل الكتب. مسح بيانات المتصفح يحذف المواضع والكتاب المحتفظ به.

حدود النسخة
- يدعم EPUB غير المحمي فقط؛ لا يزيل حماية DRM، ولا يقرأ PDF أو MOBI.
- الحد الأقصى لملف الكتاب 100 ميجابايت، وللمحتوى بعد فك الضغط 400 ميجابايت.
- نسبة التقدم تقريبية بحسب الفصل والصفحة المعروضة.
- البحث نصي بسيط، ويعرض أول 80 نتيجة، ولا يتجاهل التشكيل العربي تلقائيًا.
- الكتب ذات التخطيطات الخاصة والخطوط المشفرة قد تختلف في المظهر.
- الخطوط العربية تعتمد على الخطوط المثبتة على الجهاز.
- برامج الكتب والموارد الخارجية معطّلة.

الخصوصية
لا يجري ورق أي اتصال بالشبكة وقت التشغيل. تبقى بيانات القراءة في المتصفح،
ولا توجد خدمات تحليلات أو رفع للكتب. احتفظ بملف THIRD-PARTY-LICENSES.txt عند
إعادة توزيع الحزمة.
