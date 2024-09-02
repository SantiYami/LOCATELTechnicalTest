<template>
    <div class="home">
        <b-container>
            <b-row class="mb-3">
                <b-col>
                    <b-button @click="navigateTo('create-client')" variant="primary">Crear Cliente</b-button>
                    <b-button @click="navigateTo('create-product')" variant="secondary">Crear Producto</b-button>
                    <b-button @click="navigateTo('create-sale-header')" variant="success">Registrar Cabecera Venta</b-button>
                    <b-button @click="navigateTo('create-sale-detail')" variant="danger">Registrar Detalle Venta</b-button>
                </b-col>
            </b-row>

            <b-row>
                <b-col>
                    <b-card title="Listado de Ventas Realizadas por Fecha">
                        <b-table :items="sales" :fields="fields" striped hover>
                            <template #cell(date)="data">
                                {{ formatDate(data.value) }}
                            </template>
                            <template #cell(total_sale)="data">
                                {{ formatCurrency(data.value) }}
                            </template>
                        </b-table>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import VAPI from '@/http_common';
import { HTTP_STATUS, SERVICE_NAMES } from "@/app_constants";

export default {
    data() {
        return {
            sales: [],
            fields: [
                { key: 'consecutive', label: 'Consecutivo' },
                { key: 'date', label: 'Fecha' },
                { key: 'total_sale', label: 'Total Venta' }
            ]
        };
    },
    methods: {
        async fetchSales() {
            try {
                const response = await VAPI.get(`${SERVICE_NAMES.SALE_HEADER}/sales`);
                if (response.status === HTTP_STATUS.OK) {
                    this.sales = response.data;
                }
            } catch (error) {
                console.error(error);
            }
        },
        formatDate(date) {
            return new Date(date).toLocaleDateString();
        },
        formatCurrency(value) {
            return `$${parseFloat(value).toFixed(2)}`;
        },
        navigateTo(route) {
            this.$router.push({ name: route });
        }
    },
    mounted() {
        this.fetchSales();
    }
};
</script>

<style scoped>
.home {
    margin-top: 20px;
}
</style>
