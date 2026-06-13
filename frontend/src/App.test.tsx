import { render, screen, waitFor } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';

import App from './App';

describe('App backend health status', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('shows backend ok when the health endpoint returns ok', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({ status: 'ok' }),
      }),
    );

    render(<App />);

    expect(screen.getByText(/Backend: checking/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByText(/Backend: ok/i)).toBeInTheDocument();
    });
  });

  it('shows backend offline when the health endpoint fails', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new Error('offline')));

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/Backend: offline/i)).toBeInTheDocument();
    });
  });
});