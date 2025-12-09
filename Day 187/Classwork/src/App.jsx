// import { useState } from 'react'
import { useForm } from "react-hook-form"
import './App.css'

function App() {
  const {register, handleSubmit, watch, formState: { errors }} = useForm(
    {
      defaultValues: {
        firstName: 'L',
        lastName: 'Ch',

      }
    }
  );

  console.log(errors)
  console.log(watch())
  return (
    <div className="flex flex-col min-h-screen justify-center items-center ">
      <form className="flex flex-col justify-center items-center font-semibold w-100 h-100 border-2 border-blue-400 rounded" onSubmit={handleSubmit((data) => {
        console.log(data);
      })}>
        <h1>Login</h1>
        <input className="border-2 border-blue-300 p-1 m-2" {...register('firstName', { required: 'This is required',  })} type="text" placeholder='First Name'/>
        <input className="border-2 border-blue-300 p-1 m-2" {...register('lastName', {required: 'This is required', minLength: {
          value: 4,
          message: 'The minimum length should be 4.'
        },})} type="text" placeholder='Last Name'/>
        <p className="text-red-800">{errors?.lastName?.message}</p>
        <button type="submit" className="p-2 border border-blue-950 rounded hover:bg-blue-400 transition-colors 0.5s">Submit</button>
      </form>
    </div>
  );
}

export default App
