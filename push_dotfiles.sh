#!/bin/bash

# Папка, куда ты клонировал репозиторий
REPO_DIR=~/df

# Убедимся, что она существует
if [ ! -d "$REPO_DIR" ]; then
    echo "Ошибка: папка $REPO_DIR не найдена. Убедись, что ты клонировал репозиторий."
    exit 1
fi

# Копируем файлы и папки в репозиторий
echo "Копируем файлы..."
cp -r ~/.config/hypr "$REPO_DIR/.config/"
cp -r ~/.config/nvim "$REPO_DIR/.config/"
cp -r ~/.config/waybar "$REPO_DIR/.config/"
cp -r ~/.config/kitty "$REPO_DIR/.config/"
cp -r ~/tor-browser "$REPO_DIR/"
cp -r ~/twitch_demon "$REPO_DIR/"
cp ~/.bash_profile "$REPO_DIR/"
cp ~/.bashrc "$REPO_DIR/"
cp ~/setup.sh "$REPO_DIR/"

# Переходим в папку репозитория
cd "$REPO_DIR" || exit

# Добавляем и коммитим
echo "Добавляем изменения в git..."
git add .
git commit -m "Обновление dotfiles: $(date +'%Y-%m-%d %H:%M:%S')"

# Пушим
echo "Отправляем изменения в репозиторий..."
git push origin main

echo "✅ Готово!"

