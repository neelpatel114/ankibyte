import React, { useState } from 'react';
import axios from 'axios';

const AnkiDeckUpload = () => {
  const [file, setFile] = useState(null);
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('name', name);
    try {
      await axios.post('/api/decks/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      alert('Deck uploaded successfully');
    } catch (error) {
      console.error('Error uploading deck:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Deck Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button type="submit">Upload Deck</button>
    </form>
  );
};

export default AnkiDeckUpload;