import Prueba from './views/Example'
import PerrosPage from './views/Example2';

export default function App(props) {
    
    switch (props.page.value) {
        case "1":
            return <PerrosPage />
        
        case "2":
            return <Prueba />
    
        default:
            
            return (
                <>
                    <h1>Error de pagina</h1>
                </>
            )
    }

}