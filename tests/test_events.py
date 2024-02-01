# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Globex Corporation
# All rights reserved.
#
from maa31_ext.events import Maa31testEventsApplication


def test_handle_installation_status_change(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_installation_status_change(request)
    assert result.status == 'success'


def test_handle_asset_resume_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_resume_request_processing(request)
    assert result.status == 'success'


def test_handle_product_changed(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_product_changed(request)
    assert result.status == 'success'


def test_handle_tier_account_update_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_account_update_request_processing(request)
    assert result.status == 'success'


def test_handle_part_usage_file_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_part_usage_file_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_adjustment_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_usage_file_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_usage_file_request_processing(request)
    assert result.status == 'success'


def test_handle_listing_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_listing_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_change_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_change_request_processing(request)
    assert result.status == 'success'


def test_handle_translation_change(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_translation_change(request)
    assert result.status == 'success'


def test_handle_asset_purchase_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'


def test_handle_contract_changed(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_contract_changed(request)
    assert result.status == 'success'


def test_handle_listing_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_listing_request_processing(request)
    assert result.status == 'success'


def test_handle_pricelist_version_changed(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_pricelist_version_changed(request)
    assert result.status == 'success'


def test_handle_tier_config_setup_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_setup_request_processing(request)
    assert result.status == 'success'


def test_handle_helpdesk_case_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_helpdesk_case_processing(request)
    assert result.status == 'success'


def test_handle_asset_adjustment_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_cancel_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_cancel_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_change_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_change_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_suspend_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_suspend_request_processing(request)
    assert result.status == 'success'


def test_execute_scheduled_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Maa31testEventsApplication(connect_client, logger, config)
    result = ext.execute_scheduled_processing(request)
    assert result.status == 'success'
