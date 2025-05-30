import React, { useState } from 'react';
import './App.css';

const colorList = [
  'red', 'green', 'blue',
  'orange', 'purple', 'pink',
  'black', 'gold', 'indigo'
];

const App = () => {
  const [buttons, setButtons] = useState(Array(9).fill({ color: '', disabled: false }));
  const [colorIndex, setColorIndex] = useState(0);

  const handleClick = (index) => {
    
    if (colorIndex >= colorList.length) return;

    const updatedButtons = [...buttons];
    updatedButtons[index] = {
      color: colorList[colorIndex],
      disabled: true
    };

    setButtons(updatedButtons);
    setColorIndex(prev => prev + 1);
  };

  return (
    <div className="app">
      <h1>Button Color Grid</h1>
      <div className="grid">
        {buttons.map((btn, idx) => (
          <button
            key={idx}
            className="grid-button"
            style={{ backgroundColor: btn.color || '#ccc', cursor: btn.disabled ? 'not-allowed' : 'pointer' }}
            disabled={btn.disabled}
            onClick={() => handleClick(idx)}
          >
            {btn.disabled ? `${colorList[colorIndex]}` : 'Click Me'}
          </button>
        ))}
      </div>
      <p>
        1. Assign the next color in sequence from the colors list to the button. <br />
        2. Disable the button after it is clicked. <br />
        3. Repeat the process for subsequent button clicks
      </p>
    </div>
  );
};

export default App;
