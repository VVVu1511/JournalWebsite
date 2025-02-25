import './Header.css'


function Introduce(){
    return (
        <div className='introduce' onClick={handleClick}>
            <div>
                Introducing Nifty 3.5 🔥
            </div>

            <div className='read_blog'>
                read our blog
            </div>
        </div>
    )
}

function TaskBar(){
    return (<div className="task_bar">
        <ul>
            <li>Features</li>
            <li>Use Cases</li>
            <li>Resources</li>
            <li>Got Clients</li>
            <li>Pricing</li>
        </ul>
    </div>)
}

function Header(){
    return (
        <div className='header'>
            <Introduce />
            <TaskBar />
        </div>
    )
}

export default Header