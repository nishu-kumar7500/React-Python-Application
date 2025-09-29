import { useEffect, useState } from "react";

export default function Culture() {
  const [fact, setFact] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/fact")
      .then((res) => res.json())
      .then((data) => setFact(data.fact));
  }, []);

  return (
    <section className="culture">
      <h3>Quick Fact</h3>
      <p>{fact || "Loading a fun fact about India..."}</p>
    </section>
  );
}
