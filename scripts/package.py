from pathlib import Path
import zipfile, hashlib, json
root=Path(__file__).resolve().parent.parent
app=root/'dist'
target=root/'releases/Waraq-Portable-1.3.zip'
target.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for file in sorted(app.iterdir()):
        if file.is_file():archive.write(file,'Waraq-Portable/'+file.name)
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    assert archive.read('Waraq-Portable/Waraq.html')==(app/'Waraq.html').read_bytes()
print(json.dumps({'html_bytes':(app/'Waraq.html').stat().st_size,'zip_bytes':target.stat().st_size,'files':[f.name for f in app.iterdir() if f.is_file()],'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
