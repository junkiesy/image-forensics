import "./App.css";

function App() {
  return (
    <main className="app-shell">
      <section className="hero">
        <p className="eyebrow">Local forensic workflow</p>
        <h1>AI Image Forensics Lab</h1>
        <p className="hero-text">
          Compare real and AI-generated images, collect forensic clues, and
          build toward an AI-vs-real image detector.
        </p>
      </section>

      <section className="module-grid" aria-label="Application modules">
        <article className="module-card">
          <span className="module-number">01</span>
          <h2>Forensic Comparison Lab</h2>
          <p>
            View real and AI images side by side, zoom into details, and inspect
            visual or pixel-level differences.
          </p>
          <button type="button">Open Compare Lab</button>
        </article>

        <article className="module-card">
          <span className="module-number">02</span>
          <h2>Feature Builder</h2>
          <p>
            Save observations, extract image features, and prepare training data
            for the detector.
          </p>
          <button type="button">Open Feature Builder</button>
        </article>

        <article className="module-card">
          <span className="module-number">03</span>
          <h2>AI-Real Detector</h2>
          <p>
            Upload an image and receive an AI-vs-real prediction with a
            confidence score.
          </p>
          <button type="button">Open Detector</button>
        </article>
      </section>
    </main>
  );
}

export default App;
