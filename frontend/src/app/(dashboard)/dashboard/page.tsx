"use client";

import React from "react";
import { FaAnchor, FaShip } from "react-icons/fa";
import { Cell, Legend, Line, LineChart, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { useFetchVessels } from "@/queries/vessel";

const VesselManagementDashboard: React.FC = () => {
    const { data: vessels } = useFetchVessels();

    if (!vessels) return null;

    const pieChartData = [
        { name: "Hoạt động", value: vessels.filter(vessel => vessel.status === "Hoạt động").length, color: "#3B82F6" },
        {
            name: "Không hoạt động",
            value: vessels.filter(vessel => vessel.status === "Không hoạt động").length,
            color: "#10B981",
        },
        {
            name: "Đang Bảo Dưỡng",
            value: vessels.filter(vessel => vessel.status === "Đang bảo dưỡng").length,
            color: "#F59E0B",
        },
    ];

    const lineChartData = [
        { month: "Tháng 1", value: 4 },
        { month: "Tháng 2", value: 3 },
        { month: "Tháng 3", value: 5 },
        { month: "Tháng 4", value: 4 },
        { month: "Tháng 5", value: 6 },
        { month: "Tháng 6", value: 5 },
    ];

    return (
        <div className="container">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                <div className="bg-white p-6 rounded-lg shadow">
                    <div className="flex items-center">
                        <FaShip className="text-blue-500 text-3xl mr-4" />
                        <div>
                            <p className="text-gray-500">Tổng Số Tàu</p>
                            <p className="text-2xl font-bold">
                                {vessels.length}
                            </p>
                        </div>
                    </div>
                </div>
                <div className="bg-white p-6 rounded-lg shadow">
                    <div className="flex items-center">
                        <FaAnchor className="text-green-500 text-3xl mr-4" />
                        <div>
                            <p className="text-gray-500">Tàu Đã Cập Bến</p>
                            <p className="text-2xl font-bold">
                                {
                                    vessels.filter(
                                        vessel =>
                                            vessel.status ===
                                            "Không hoạt động",
                                    ).length
                                }
                            </p>
                        </div>
                    </div>
                </div>
                <div className="bg-white p-6 rounded-lg shadow">
                    <div className="flex items-center">
                        <FaShip className="text-blue-500 text-3xl mr-4" />
                        <div>
                            <p className="text-gray-500">
                                Tàu Đang Vận Chuyển
                            </p>
                            <p className="text-2xl font-bold">
                                {
                                    vessels.filter(
                                        vessel =>
                                            vessel.status === "Hoạt động",
                                    ).length
                                }
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                <div className="bg-white p-6 rounded-lg shadow">
                    <h2 className="text-xl font-bold mb-4">
                        Phân Phối Trạng Thái Tàu
                    </h2>
                    <div className="h-64">
                        <ResponsiveContainer>
                            <PieChart>
                                <Pie
                                    data={pieChartData}
                                    dataKey="value"
                                    nameKey="name"
                                    cx="50%"
                                    cy="50%"
                                    outerRadius={80}
                                >
                                    {pieChartData.map((entry, index) => (
                                        <Cell key={`cell-${index}`} fill={entry.color} />
                                    ))}
                                </Pie>
                                <Tooltip />
                                <Legend />
                            </PieChart>
                        </ResponsiveContainer>
                    </div>
                </div>
                <div className="bg-white p-6 rounded-lg shadow">
                    <h2 className="text-xl font-bold mb-4">
                        Xu Hướng Vận Chuyển Hàng Tháng
                    </h2>
                    <div className="h-64">
                        <ResponsiveContainer>
                            <LineChart data={lineChartData}>
                                <XAxis dataKey="month" />
                                <YAxis />
                                <Tooltip />
                                <Legend />
                                <Line
                                    type="monotone"
                                    dataKey="value"
                                    stroke="#3B82F6"
                                />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow">
                <h2 className="text-xl font-bold mb-4">
                    Theo Dõi Thời Gian Thực
                </h2>
                <div className="h-96 bg-gray-100 flex items-center justify-center">
                    <p className="text-gray-500">
                        Đang Xây Dựng Thành Phần Bản Đồ
                    </p>
                </div>
            </div>
        </div>
    );
};

export default VesselManagementDashboard;