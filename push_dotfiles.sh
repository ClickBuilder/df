#!/bin/bash

REPO_DIR=~/df

if [ ! -d "$REPO_DIR" ]; then
    echo "Ошибка: папка $REPO_DIR не найдена."
    exit 1
fi

echo "Копируем файлы..."
cp -r ~/.config/hypr "$REPO_DIR/"
cp -r ~/.config/nvim "$REPO_DIR/"
cp -r ~/.config/waybar "$REPO_DIR/"
cp -r ~/.config/kitty "$REPO_DIR/"
cp -r ~/twitch_demon "$REPO_DIR/"
cp ~/.bash_profile "$REPO_DIR/"
cp ~/.bashrc "$REPO_DIR/"
cp ~/setup.sh "$REPO_DIR/"

cd "$REPO_DIR" || exit


echo "Добавляем изменения в git..."
git add .
git commit -m "Обновление dotfiles: $(date +'%Y-%m-%d %H:%M:%S')" || echo "Нет новых изменений."

echo "Отправляем изменения в репозиторий..."
git push origin main

echo "✅ Готово!"

