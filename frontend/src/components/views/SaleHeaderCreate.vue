<template>
    <div class="create-sale-header">
        <b-container>
            <b-row class="justify-content-md-center">
                <b-col md="6">
                    <b-card title="Registrar Cabecera de Venta">
                        <b-form @submit.prevent="handleSubmit">
                            <b-form-group label="Fecha de Venta:" label-for="date">
                                <b-form-datepicker
                                id="date"
                                v-model="sale.date"
                                required
                                ></b-form-datepicker>
                            </b-form-group>

                            <b-form-group label="Cliente:" label-for="user_id">
                                <b-form-input
                                id="user_id"
                                v-model="sale.user_id"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="Total Venta:" label-for="total_sale">
                                <b-form-input
                                id="total_sale"
                                v-model="sale.total_sale"
                                type="number"
                                step="0.01"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group>
                                <b-button type="submit" variant="primary">Registrar Venta</b-button>
                            </b-form-group>
                        </b-form>
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
        sale: {
            date: '',
            user_id: '',
            total_sale: ''
        }
        };
    },
    methods: {
        async handleSubmit() {
        try {
            const response = await VAPI.post(`${SERVICE_NAMES.SALE_HEADER}/sales`, this.sale);
            if (response.status === HTTP_STATUS.CREATED) {
                this.$toast.success('Cabecera de venta registrada exitosamente');
                this.$router.push('/');
            }
        } catch (error) {
            this.$toast.error('Error al registrar la cabecera de venta');
        }
        }
    }
};
</script>

<style scoped>
.create-sale-header {
    margin-top: 20px;
}
</style>
