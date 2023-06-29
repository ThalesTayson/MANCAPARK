cd react-mancapark
npm run build
cd ..
Remove-Item -Path ".\statics-files\js\main.js" -Force
Copy-Item -Path ".\react-mancapark\dist\bundle.js" -Destination ".\statics-files\js"
Rename-Item -Path ".\statics-files\js\bundle.js" -NewName "main.js"