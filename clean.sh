# 该脚本是为了快速删除静态文件，方便更新前端内容。
echo "删除 /static/js 文件夹 中..."
git rm -r ./static/js
echo "删除 /static/css 文件夹 中..."
git rm -r ./static/css
echo "删除 /template/index.html 中..."
git rm -r ./template/index.html
echo "git add"
git add .
echo "git commit"
git commit -m "clean old frontend files"
echo "git push"
git push origin master
echo "完成！"