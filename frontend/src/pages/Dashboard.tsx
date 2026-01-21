import React, { useEffect, useState } from 'react';
import api from '../services/api';

interface Subject {
    name: string;
    code: string;
    time: string;
    location: string;
    day_of_week: number;
}

const Dashboard: React.FC = () => {
    const [subjects, setSubjects] = useState<Subject[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchSchedule = async () => {
            try {
                // Giả sử có 1 student_id mẫu hoặc lấy từ token
                const response = await api.get('/schedules/test_student_id');
                setSubjects(response.data.subjects || []);
            } catch (err) {
                console.error('Lỗi tải lịch học:', err);
            } finally {
                setLoading(false);
            }
        };
        fetchSchedule();
    }, []);

    const days = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ Nhật'];

    return (
        <div className="p-6 bg-slate-50 min-h-screen">
            <header className="flex justify-between items-center mb-8 bg-white p-4 rounded-xl shadow-sm border border-slate-100">
                <h1 className="text-2xl font-bold text-slate-800">Lịch Học Của Tôi</h1>
                <button
                    onClick={() => { localStorage.clear(); window.location.href = '/login'; }}
                    className="text-red-500 hover:bg-red-50 px-4 py-2 rounded-lg transition-colors"
                >
                    Đăng xuất
                </button>
            </header>

            {loading ? (
                <p>Đang tải...</p>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-7 gap-4">
                    {days.map((day, index) => (
                        <div key={day} className="bg-white p-4 rounded-xl shadow-sm border border-slate-100 min-h-[300px]">
                            <h3 className="font-semibold text-blue-600 mb-4 border-b pb-2">{day}</h3>
                            <div className="space-y-3">
                                {subjects.filter(s => s.day_of_week === index + 2).map((sub, i) => (
                                    <div key={i} className="bg-blue-50 p-3 rounded-lg border border-blue-100">
                                        <p className="font-bold text-blue-800 text-sm">{sub.name}</p>
                                        <p className="text-xs text-blue-600 mt-1">{sub.time}</p>
                                        <p className="text-xs text-slate-500 mt-1 italic">{sub.location}</p>
                                    </div>
                                ))}
                                {subjects.filter(s => s.day_of_week === index + 2).length === 0 && (
                                    <p className="text-xs text-slate-300 italic text-center py-4">Trống</p>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Dashboard;
