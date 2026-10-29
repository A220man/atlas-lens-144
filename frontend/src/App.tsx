import { useState, useEffect } from 'react'
import { Plugin } from './types'
import PluginList from './PluginList'
import PluginDetail from './PluginDetail'
import './App.css'

function App() {
  const [plugins, setPlugins] = useState<Plugin[]>([])
  const [selectedPlugin, setSelectedPlugin] = useState<Plugin | null>(null)
  const [search, setSearch] = useState('')
  const [category, setCategory] = useState<string>('all')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchPlugins()
  }, [])

  const fetchPlugins = async () => {
    try {
      const response = await fetch('/api/plugins')
      if (!response.ok) throw new Error('Failed to fetch plugins')
      const data = await response.json()
      setPlugins(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error')
    } finally {
      setLoading(false)
    }
  }

  const filteredPlugins = plugins.filter(plugin => {
    const matchesSearch = plugin.name.toLowerCase().includes(search.toLowerCase()) ||
      plugin.description.toLowerCase().includes(search.toLowerCase())
    const matchesCategory = category === 'all' || plugin.category === category
    return matchesSearch && matchesCategory
  })

  const categories = ['all', ...new Set(plugins.map(p => p.category))]

  if (loading) return <div className="loading">Loading plugins...</div>
  if (error) return <div className="error">Error: {error}</div>

  return (
    <div className="app">
      <header>
        <h1>atlas-lens-144</h1>
        <p>Official Claude Code Plugins Marketplace</p>
      </header>
      <main>
        <div className="controls">
          <input
            type="text"
            placeholder="Search plugins..."
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
          <select value={category} onChange={e => setCategory(e.target.value)}>
            {categories.map(c => (
              <option key={c} value={c}>
                {c === 'all' ? 'All Categories' : c.toUpperCase()}
              </option>
            ))}
          </select>
        </div>
        <div className="content">
          <PluginList
            plugins={filteredPlugins}
            onSelect={setSelectedPlugin}
            selected={selectedPlugin}
          />
          {selectedPlugin && (
            <PluginDetail plugin={selectedPlugin} onClose={() => setSelectedPlugin(null)} />
          )}
        </div>
      </main>
    </div>
  )
}

export default App
