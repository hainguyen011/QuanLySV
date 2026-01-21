import React, { useState } from 'react';
import api from '../services/api';

const Login: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);

            const response = await api.post('/auth/login', formData);
            localStorage.setItem('token', response.data.access_token);
            window.location.href = '/dashboard';
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Đăng nhập thất bại');
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-50">
            <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md border border-slate-100">
                <h1 className="text-3xl font-bold text-slate-800 mb-2 text-center">QuanLySV</h1>
                <p className="text-slate-500 text-center mb-8">Hệ thống quản lý lịch học sinh viên</p>

                <form onSubmit={handleLogin} className="space-y-6">
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">Tài khoản</label>
                        <input
                            type="text"
                            className="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                            placeholder="Nhập username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-slate-700 mb-1">Mật khẩu</label>
                        <input
                            type="password"
                            className="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                            placeholder="••••••••"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>

                    {error && <p className="text-red-500 text-sm text-center">{error}</p>}

                    <button
                        type="submit"
                        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-colors shadow-lg shadow-blue-200"
                    >
                        Đăng nhập
                    </button>
                </form>

                <p className="mt-6 text-center text-sm text-slate-600">
                    Chưa có tài khoản? <a href="/register" className="text-blue-600 font-semibold hover:underline">Đăng ký ngay</a>
                </p>
            </div>
        </div>
    );
};

export default Login;
