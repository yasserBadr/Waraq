from pathlib import Path
import zipfile, hashlib, json

FIXED_ZIP_TIME=(2026, 10, 29, 0, 0, 0)

root=Path(__file__).resolve().parent.parent
app=root/'dist'
VERSION=(root/'VERSION').read_text(encoding='utf-8').strip()
target=root/f'releases/Waraq-Portable-{VERSION}.zip'
target.parent.mkdir(exist_ok=True)

with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for file in sorted(app.iterdir()):
        if not file.is_file():
            continue
        info=zipfile.ZipInfo('Waraq-Portable/'+file.name,FIXED_ZIP_TIME)
        info.create_system=3
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o644 << 16
        archive.writestr(info,file.read_bytes())

with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    assert archive.read('Waraq-Portable/Waraq.html')==(app/'Waraq.html').read_bytes()
    assert all(info.date_time==FIXED_ZIP_TIME for info in archive.infolist())

print(json.dumps({'version':VERSION,'html_bytes':(app/'Waraq.html').stat().st_size,'zip_bytes':target.stat().st_size,'files':[f.name for f in sorted(app.iterdir()) if f.is_file()],'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
