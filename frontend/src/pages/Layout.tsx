import { Outlet } from "react-router-dom";
import { Footer } from "../components/Footer";
import { Header } from "../components/Header";

export function Layout(){
    return(
        <>
        <Header/>
        <main className="flex-grow">
            <Outlet/>
        </main>
        <Footer/>
        </>
    )
}