import { useForm } from "react-hook-form"


function App() {
    const {register, handleSubmit, formState: { errors }} = useForm();

  console.log(errors)

  return (
    <div>
      <div className='flex flex-col min-h-screen justify-center items-center border-b-blue-300 border-2'>
        <h1 className="size-10">Login</h1>
        <form className=' flex flex-col justify-center items-center m-5' onSubmit={handleSubmit((data) => {
        console.log(data);
      })}>
          <input className="p-2 rounded-xs border-white" type="text" placeholder='fullName' {...register('firstName', { required: 'This is required',  })}/>
          <input className="p-2 rounded-xs border-white" type="password" placeholder='Password' {...register('lastName', {required: 'This is required', minLength: {
          value: 4,
          message: 'The minimum length should be 4.'
        },})} />
          <p className="text-red-700">{errors?.lastName?.message}</p>
          <button type="submit">Submit</button>
        </form>

      </div>
    </div>
  )
}

export default App
