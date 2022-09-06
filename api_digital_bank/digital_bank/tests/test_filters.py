

from rest_framework.test import APITestCase

from digital_bank.support_code.filter_test import post_tranfers, post_tranfers_id


class FiltersTestCase(APITestCase):
    """ Essa classe realiza os testes sobre as ações possíveis em relação aos
    as consultas de transferências."""


    def test_transfers_received(self):
        id = post_tranfers_id(self)

        response = self.client.get(
            f'/consulta/?favored_costumer={id}', format='json')

        self.assertTrue(response.data["count"] == 2)

    def test_transfers_sent(self):

        id = post_tranfers_id(self)
        response = self.client.get(
            f'/consulta/?requesting_costumer={id}', format='json')

        self.assertTrue(response.data["count"] == 1)

    # def test_transfers_between_for_costumer(self):

    #     id = post_tranfers_id(self)
    #     response = self.client.get(
    #         f'/consulta/?date__gte=2022-01-01T00:00:00&date__lte=2022-12-30T23:59:59&requesting_costumer={id}', format='json')

    #     self.assertTrue(response.data["count"] == 1)

    # def test_transfers_between(self):

    #     post_tranfers(self)

    #     response = self.client.get(
    #         '/consulta/?date__gte=2022-06-18T00:00:00&date__lte=2022-12-30T23:59:59', format='json')

    #     self.assertTrue(response.data["count"] == 2)