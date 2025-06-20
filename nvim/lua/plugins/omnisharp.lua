return {
  "OmniSharp/omnisharp-vim",
  config = function()
    require("lspconfig").omnisharp.setup {}
  end,
}
