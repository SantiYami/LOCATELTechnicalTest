<template>
    <div class="create-sale-detail">
        <b-container>
            <b-row class="justify-content-md-center">
                <b-col md="6">
                    <b-card title="Registrar Detalle de Venta">
                        <b-form @submit.prevent="handleSubmit">
                            <b-form-group label="ID de Venta:" label-for="sale_id">
                                <b-form-input
                                id="sale_id"
                                v-model="saleDetail.sale_id"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="ID del Producto:" label-for="product_id">
                                <b-form-input
                                id="product_id"
                                v-model="saleDetail.product_id"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="Valor del Producto:" label-for="product_value">
                                <b-form-input
                                id="product_value"
                                v-model="saleDetail.product_value"
                                type="number"
                                step="0.01"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="IVA Calculado:" label-for="iva_calculated">
                                <b-form-input
                                id="iva_calculated"
                                v-model="saleDetail.iva_calculated"
                                type="number"
                                step="0.01"
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group>
                                <b-button type="submit" variant="primary">Registrar Detalle</b-button>
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
        saleDetail: {
            sale_id: '',
            product_id: '',
            product_value: '',
            iva_calculated: ''
        }
        };
    },
    methods: {
        async handleSubmit() {
        try {
            const response = await VAPI.post(`${SERVICE_NAMES.SALE_DETAIL}/sale-details`, this.saleDetail);
            if (response.status === HTTP_STATUS.CREATED) {
                this.$toast.success('Detalle de venta registrado exitosamente');
                this.$router.push('/');
            }
        } catch (error) {
            this.$toast.error('Error al registrar el detalle de venta');
        }
        }
    }
};
</script>

<style scoped>
.create-sale-detail {
    margin-top: 20px;
}
</style>
