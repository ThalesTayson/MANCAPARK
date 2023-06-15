cd react-mancapark
npm run build
cd ..
Remove-Item -Path ".\WEB\static\js\bundle.js" -Force
Copy-Item -Path ".\react-mancapark\dist\bundle.js" -Destination ".\WEB\static\js"