// import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createRoutesFromElements, Route } from 'react-router-dom'
import App from './components/App'
import Home from './components/Home'

export const routes = createRoutesFromElements(
  <Route path="/" element={<App />}>
    <Route index element={<Home />} />
  </Route>
)
