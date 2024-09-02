<template>
    <div class="create-product">
        <b-container>
            <b-row class="justify-content-md-center">
                <b-col md="6">
                    <b-card title="Crear Producto">
                        <b-form @submit.prevent="handleSubmit">
                            <b-form-group label="Código:" label-for="code">
                                <b-form-input
                                id="code"
                                v-model="product.code"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="Nombre:" label-for="name">
                                <b-form-input
                                id="name"
                                v-model="product.name"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="Valor de Venta:" label-for="sale_value">
                                <b-form-input
                                id="sale_value"
                                v-model="product.sale_value"
                                type="number"
                                step="0.01"
                                required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group label="Maneja IVA:" label-for="handles_iva">
                                <b-form-checkbox
                                id="handles_iva"
                                v-model="product.handles_iva"
                                >Sí</b-form-checkbox>
                            </b-form-group>

                            <b-form-group v-if="product.handles_iva" label="Porcentaje IVA:" label-for="iva_percentage">
                                <b-form-input
                                id="iva_percentage"
                                v-model="product.iva_percentage"
                                type="number"
                                step="0.01"
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group>
                                <b-button type="submit" variant="primary">Crear Producto</b-button>
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
        product: {
            code: '',
            name: '',
            sale_value: '',
            handles_iva: false,
            iva_percentage: ''
        }
        };
    },
    methods: {
        async handleSubmit() {
        try {
            const response = await VAPI.post(`${SERVICE_NAMES.PRODUCT}/product`, this.product);
            if (response.status === HTTP_STATUS.CREATED) {
                this.$toast.success('Producto creado exitosamente');
                this.$router.push('/');
            }
        } catch (error) {
            this.$toast.error('Error al crear el producto');
        }
        }
    }
};
</script>

<style scoped>
.create-product {
     margin-top: 20px;
}
</style>
