python -m ok.update.package_launcher "v1.0" deploy.txt
Copy-Item -Path "dist" -Destination "ok-ww" -Recurse
7z a -t7z -r "ok-ww-v1.0.7z" "ok-ww"     
Remove-Item -Path "ok-ww" -Recurse -Force