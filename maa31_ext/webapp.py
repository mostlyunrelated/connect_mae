# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Globex Corporation
# All rights reserved.
#
from typing import List

from connect.client import ConnectClient, R
from connect.eaas.core.decorators import (
    router,
    variables,
    web_app,
)
from logging import LoggerAdapter

from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.inject.common import get_call_context
from connect.eaas.core.inject.models import Context
from connect.eaas.core.inject.synchronous import get_installation, get_installation_client
from connect.eaas.core.inject.common import get_logger
from fastapi import Depends

from maa31_ext.schemas import Marketplace, Settings


@variables([
    {
        'name': 'VAR_NAME_1',
        'initial_value': 'VAR_VALUE_1',
        'secure': False,
    },
    {
        'name': 'VAR_NAME_N',
        'initial_value': 'VAR_VALUE_N',
        'secure': True,
    },
])
@web_app(router)
class Maa31testWebApplication(WebApplicationBase):

    #@classmethod
    #def on_startup(cls, logger: LoggerAdapter, config: dict):
    #    logger.info('Hi from on startup method')


    @router.get(
        '/test',
        summary='test endpoint',
    )
    def test_method(
        self,
        client: ConnectClient = Depends(get_installation_client),
        logger: LoggerAdapter = Depends(get_logger),
    ):  
        logger.info("Hi from get method")
        return
        '''
        return [
            Marketplace(**marketplace)
            for marketplace in client.marketplaces.all().values_list(
                'id', 'name', 'description', 'icon',
            )
        ]
        '''

    @router.get(
        '/settings',
        summary='Retrieve charts settings',
        response_model=Settings,
    )
    def retrieve_settings(
        self,
        installation: dict = Depends(get_installation),
    ):
        return Settings(marketplaces=installation['settings'].get('marketplaces', []))

    @router.post(
        '/settings',
        summary='Save charts settings',
        response_model=Settings,
    )
    def save_settings(
        self,
        settings: Settings,
        context: Context = Depends(get_call_context),
        client: ConnectClient = Depends(get_installation_client),
    ):
        client('devops').installations[context.installation_id].update(
            payload={
                'settings': settings.dict(),
            },
        )
        return settings

    @router.get(
        '/chart',
        summary='Generate chart data',
    )
    def generate_chart_data(
        self,
        installation: dict = Depends(get_installation),
        client: ConnectClient = Depends(get_installation_client),
    ):
        data = {}
        for mp in installation['settings'].get('marketplaces', []):
            active_assets = client('subscriptions').assets.filter(
                R().marketplace.id.eq(mp['id']) & R().status.eq('active'),
            ).count()
            data[mp['id']] = active_assets

        return {
            'type': 'bar',
            'data': {
                'labels': list(data.keys()),
                'datasets': [
                    {
                        'label': 'Subscriptions',
                        'data': list(data.values()),
                    },
                ],
            },
        }
