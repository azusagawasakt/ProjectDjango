import { Medal } from "lucide-react";

const MarketingPage = () => {
    return (
        <div className="flex items-center justify-center flex-col">
            <div className="flex items-center justify-center flex-col">
                <div className="mb-4 flex items-center border shadow-sm p-4 bg-amber-100 text-amber-700 rounded-full uppercase">
                    <Medal className="h-6 w-6 mr-2" />
                    No 1 task managment
                </div>
                <h1>
                    Taskify helps team move
                </h1>
            </div>
        </div>
    )
}

export default MarketingPage;