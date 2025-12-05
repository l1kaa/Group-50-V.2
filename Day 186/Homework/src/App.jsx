import React, { useState, useMemo } from 'react';

const items = [
  'javascript', 'python', 'java', 'c++', 'c#', 'go', 'rust', 'php', 'swift', 'kotlin',
  'typescript', 'ruby', 'sql', 'dart', 'bash', 'perl', 'scala', 'haskell', 'elixir', 'clojure',
  'react', 'vue', 'angular', 'svelte', 'nextjs', 'nuxt', 'nodejs', 'express', 'django', 'flask',
  'spring', 'laravel', 'fastapi', 'nest', 'deno', 'bun', 'redux', 'zustand', 'tailwind', 'bootstrap',
  'html', 'css', 'sass', 'less', 'webpack', 'vite', 'babel', 'eslint', 'prettier', 'jest',
  'mocha', 'chai', 'cypress', 'playwright', 'postman', 'graphql', 'rest', 'mongodb', 'mysql', 'postgres',
  'firebase', 'supabase', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'github', 'gitlab',
  'linux', 'ubuntu', 'windows', 'macos', 'android', 'ios', 'figma', 'photoshop', 'illustrator', 'xd',
  'blender', 'unity', 'unreal', 'threejs', 'pandas', 'numpy', 'tensorflow', 'pytorch', 'opencv', 'matlab',
  'cybersecurity', 'blockchain', 'ai', 'ml', 'nlp', 'devops', 'testing', 'ui/ux', 'api', 'json'
];
function App() {
  const [item, searchItem] = useState('');
  const search = useMemo(() => {
    return items.filter(i => 
      i.toLowerCase().includes(item.toLowerCase())
    )
  }, [item])
  
  return (
    <div className='flex justify-center items-start min-h-screen bg-gray-200 py-10'>
      <div className='w-full max-w-lg bg-white p-6 rounded-lg shadow-md'>
        <label htmlFor="inp" className='block mb-2 font-medium'>Enter a text:</label>
        <input 
          id='inp' 
          type="text" 
          className='w-full border-2 border-gray-300 p-2 rounded mb-4'
          onChange={e => searchItem(e.target.value)}
        />
        <ul className='space-y-2 max-h-96 overflow-y-auto'>
          {search.map((i) => (
            <li 
              key={i} 
              className='p-2 bg-gray-100 rounded hover:bg-gray-200 transition'
            >
              {i}
            </li>
          ))}
        </ul>
      </div>
    </div>

  );
}

export default App;