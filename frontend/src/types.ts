export interface Plugin {
  name: string
  description: string
  author: string
  source: string
  category: 'lsp' | 'mcp' | 'tool' | 'other'
  tags: string[]
  lspServers?: Record<string, unknown>
  mcpServers?: Record<string, unknown>
}
