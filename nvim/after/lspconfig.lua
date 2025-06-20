local capabilities = require("cmp_nvim_lsp").default_capabilities()
require("lspconfig").omnisharp.setup {
  -- настройки для OmniSharp
  cmd = { "/usr/bin/omnisharp", "--stdio" },
  filetypes = { "cs" },
  capabilities = capabilities,
}

