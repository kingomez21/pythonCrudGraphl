const {useState} = React


function App() {

    const [nom, setNom] = useState('')

    const changeNombre = (e) => {
        setNom(e.target.value)
        console.log(nom)
    }

    return (
        <>
            <form action="">
                <input type="text" id="nombre" onChange={changeNombre} />
            </form>
            <p>estoy desde un componente react</p>
        </>
    )
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);