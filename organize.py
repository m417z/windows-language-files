import shutil
import subprocess
import tempfile
import time
from pathlib import Path

SRC_DIR = R"C:\Sources\winbindex-data-insider\manifests\builds\92ec64ac-7c04-4309-b3cc-50e40cbcb609"
RESOURCE_HACKER = R"C:\Program Files (x86)\Resource Hacker\ResourceHacker.exe"
PRI_INFO = R"C:\Sources\PriTools\PriInfo\bin\Debug\net8.0\PriInfo.exe"


def handle_res(src: Path, dst: Path):
    assert not dst.exists(), dst

    dst.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_src = Path(tmp, src.name)
        tmp_dst = Path(tmp, src.name + '.rc')

        # Copy to temp and use the \\?\ prefix to make it work with long paths.
        shutil.copyfile('\\\\?\\' + str(src.resolve()), tmp_src)

        cmd = [
            RESOURCE_HACKER,
            "-open",
            tmp_src,
            "-save",
            tmp_dst,
            "-action",
            "extract",
            "-mask",
            ",,",
        ]
        subprocess.check_call(cmd)

        dst_rc = dst.with_name(dst.name + ".rc")
        shutil.copyfile(tmp_dst, '\\\\?\\' + str(dst_rc.resolve()))


def handle_pri(src: Path, dst: Path):
    assert not dst.exists(), dst

    dst.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        PRI_INFO,
        src,
    ]
    data = subprocess.check_output(cmd)

    dst.write_bytes(data)


start_time = time.time()

for p in Path(SRC_DIR).rglob('*'):
    if p.is_dir():
        continue

    ext = p.suffix
    path_rel = p.relative_to(SRC_DIR)

    if ext in ('.dll', '.mui'):
        handle_res(p, path_rel)
        continue

    if ext in ('.pri'):
        handle_pri(p, path_rel)
        continue

end_time = time.time()

print(f"Finished in {end_time - start_time} seconds")
