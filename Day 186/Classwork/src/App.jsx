import { useState, useMemo } from 'react';


const App = () => {
  const [count, setCount] = useState(0);
  const [count2, setCount2] = useState(0);
  const calculation = useMemo(() => calc(count), [count]);

  const increment = () => {
    setCount((c) => c + 1);
  };

  const increment2 = () => {
    setCount2((c2) => c2 + 1);
  };


  return (
    <div>
      <div>
        <button onClick={increment}>+</button> <br /><br />
        Count: {count}
        <h2>Result</h2>
        {calculation}

      <hr />
        <button onClick={increment2}>+</button> <br /><br />
        Count: {count2}
      </div>
    </div>
  );
};

const calc = (num) => {
  console.log("Calculating...");
  for (let i = 0; i < 1000000000; i++) {
    num += 1;
  }
  return num;
};



export default App;