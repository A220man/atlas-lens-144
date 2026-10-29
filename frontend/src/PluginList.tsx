import { Plugin } from './types'

interface PluginListProps {
  plugins: Plugin[]
  onSelect: (plugin: Plugin) => void
  selected: Plugin | null
}

export default function PluginList({ plugins, onSelect, selected }: PluginListProps) {
  return (
    <div className="plugin-list">
      <h2>Plugins ({plugins.length})</h2>
      <ul>
        {plugins.map(plugin => (
          <li
            key={plugin.name}
            className={selected?.name === plugin.name ? 'selected' : ''}
            onClick={() => onSelect(plugin)}
          >
            <div className="plugin-info">
              <h3>{plugin.name}</h3>
              <p>{plugin.description}</p>
              <div className="plugin-meta">
                <span className="category">{plugin.category.toUpperCase()}</span>
                <span className="author">by {plugin.author}</span>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
