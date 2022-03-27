import ReactDOM from "react-dom";
import App from './App';

const renderPage = document.getElementById('type')

if(renderPage){
    ReactDOM.render(
        <App page={renderPage}/>,
        document.getElementById('root')
    );
}else {
    ReactDOM.render(
        <h1>ERROR OF TYPE</h1>,
        document.getElementById('root')
    );
}



