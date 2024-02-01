# -*- coding: utf-8 -*-
#
# Copyright (c) 2024, Globex Corporation
# All rights reserved.
#
from connect.eaas.core.decorators import (
    event,
    schedulable,
    variables,
)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
    ScheduledExecutionResponse,
)


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
class Maa31testEventsApplication(EventsApplicationBase):
    @event(
        'installation_status_change',
        statuses=[
            'installed', 'uninstalled',
        ],
    )
    def handle_installation_status_change(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_resume_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_resume_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'product_changed',
        statuses=[
            'draft', 'indevelopment', 'oncertification',
            'published', 'initializationfailed', 'deleted',
            'endofsale',
        ],
    )
    def handle_product_changed(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_account_update_request_processing',
        statuses=[
            'pending', 'accepted', 'ignored',
        ],
    )
    def handle_tier_account_update_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'part_usage_file_request_processing',
        statuses=[
            'draft', 'ready', 'closed',
            'failed',
        ],
    )
    def handle_part_usage_file_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_adjustment_request_processing',
        statuses=[
            'draft', 'pending', 'approved',
            'failed', 'inquiring',
        ],
    )
    def handle_tier_config_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'usage_file_request_processing',
        statuses=[
            'draft', 'uploading', 'uploaded',
            'invalid', 'processing', 'ready',
            'rejected', 'pending', 'accepted',
            'closed',
        ],
    )
    def handle_usage_file_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'listing_processing',
        statuses=[
            'unlisted', 'listed',
        ],
    )
    def handle_listing_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_change_request_processing',
        statuses=[
            'draft', 'pending', 'approved',
            'failed', 'inquiring',
        ],
    )
    def handle_tier_config_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'translation_change',
        statuses=[
            
        ],
    )
    def handle_translation_change(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_purchase_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_purchase_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'contract_changed',
        statuses=[
            'new', 'enrolling', 'pending',
            'active', 'terminated', 'rejected',
        ],
    )
    def handle_contract_changed(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'listing_request_processing',
        statuses=[
            'draft', 'reviewing', 'deploying',
            'completed', 'canceled',
        ],
    )
    def handle_listing_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'pricelist_version_changed',
        statuses=[
            'draft', 'processing', 'scheduled',
            'active', 'expired',
        ],
    )
    def handle_pricelist_version_changed(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_setup_request_processing',
        statuses=[
            'draft', 'pending', 'approved',
            'failed', 'inquiring',
        ],
    )
    def handle_tier_config_setup_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'helpdesk_case_processing',
        statuses=[
            'pending', 'inquiring', 'resolved',
            'closed',
        ],
    )
    def handle_helpdesk_case_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_adjustment_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_cancel_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_cancel_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_change_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_suspend_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_suspend_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @schedulable('Schedulable method', 'It can be used to test DevOps scheduler.')
    def execute_scheduled_processing(self, schedule):
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()
