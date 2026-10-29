import { Plugin } from './types'

interface PluginDetailProps {
  plugin: Plugin
  onClose: () => void
}

export default function PluginDetail({ plugin, onClose }: PluginDetailProps) {
  return (
    <div className="plugin-detail">
      <div className="detail-header">
        <h2>{plugin.name}</h2>
        <button onClick={onClose} className="close-btn">×</button>
      </div>
      <p className="description">{plugin.description}</p>
      
      <div className="detail-section">
        <h3>Metadata</h3>
        <dl>
          <dt>Author</dt>
          <dd>{plugin.author}</dd>
          <dt>Category</dt>
          <dd>{plugin.category.toUpperCase()}</dd>
          <dt>Tags</dt>
          <dd>{plugin.tags.join(', ')}</dd>
          <dt>Source</dt>
          <dd><a href={plugin.source} target="_blank" rel="noopener noreferrer">{plugin.source}</a></dd>
        </dl>
      </div>

      {plugin.lspServers && (
        <div className="detail-section">
          <h3>LSP Configuration</h3>
          <pre>{JSON.stringify(plugin.lspServers, null, 2)}</pre>
        </div>
      )}

      {plugin.mcpServers && (
        <div className="detail-section">
          <h3>MCP Configuration</h3>
          <pre>{JSON.stringify(plugin.mcpServers, null, 2)}</pre>
        </div>
      )}

      <div className="detail-section">
        <h3>Installation</h3>
        <p>To install this plugin in Claude Code:</p>
        <pre>{`claude plugins install ${plugin.name}@claude-plugins-official`}</pre>
      </div>
    </div>
  )
}
