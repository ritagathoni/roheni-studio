from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1];d=p/'assets/video';d.mkdir(exist_ok=True);t=p/'private/material-film-build';t.mkdir(exist_ok=True)
for i,n in enumerate(['board-denim.png','board-hide-original.png','board-leather.png']):
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(p/'assets/images'/n),'-vf',"scale=1200:-1,crop=960:720,zoompan=z='1.04+0.0004*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=72:s=960x720:fps=24,format=yuv420p",'-frames:v','72','-c:v','libx264','-preset','fast','-crf','24',str(t/f'{i}.mp4')],check=True)
(t/'concat.txt').write_text(''.join(f"file '{i}.mp4'\n" for i in range(3)))
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(t/'concat.txt'),'-c','copy','-movflags','+faststart',str(d/'material-study.mp4')],check=True)
print('Video bytes', (d/'material-study.mp4').stat().st_size)
