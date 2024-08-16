import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AnkiDeckList = () => {
  const [decks, setDecks] = useState([]);

  useEffect(() => {
    const fetchDecks = async () => {
      const res = await axios.get('/api/decks/');
      setDecks(res.data);
    };
    fetchDecks();
  }, []);

  return (
    <div>
      <h2>Anki Decks</h2>
      <ul>
        {decks.map(deck => (
          <li key={deck.id}>{deck.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default AnkiDeckList;