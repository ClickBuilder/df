require("mux")
-- Включить lazy.nvim
require("config.lazy")
-- Включить поддержку системного буфера обмена в Wayland
vim.opt.clipboard = "unnamedplus"
vim.cmd [[source ~/.config/nvim/after/telescope.lua]]
vim.cmd [[source ~/.config/nvim/after/tree-sitter.lua]]
vim.cmd [[source ~/.config/nvim/after/omnisharp.lua]]
vim.cmd [[source ~/.config/nvim/after/lspconfig.lua]]

