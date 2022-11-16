# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: event.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

import betterproto

from . import proto_types


@dataclass
class Event(betterproto.Message):
    """Event containing standard fields and detail sub-events"""

    msg: str = betterproto.string_field(1)
    level: str = betterproto.string_field(2)
    invocation_id: str = betterproto.string_field(3)
    pid: int = betterproto.int32_field(4)
    thread: str = betterproto.string_field(5)
    ts: datetime = betterproto.message_field(9)
    code: str = betterproto.string_field(10)
    name: str = betterproto.string_field(11)
    extra: Dict[str, str] = betterproto.map_field(
        12, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    main_report_version: proto_types.MainReportVersion = betterproto.message_field(
        101, group="detail"
    )
    main_report_args: proto_types.MainReportArgs = betterproto.message_field(
        102, group="detail"
    )
    main_tracking_user_state: proto_types.MainTrackingUserState = (
        betterproto.message_field(103, group="detail")
    )
    merged_from_state: proto_types.MergedFromState = betterproto.message_field(
        104, group="detail"
    )
    missing_profile_target: proto_types.MissingProfileTarget = (
        betterproto.message_field(105, group="detail")
    )
    invalid_vars_yaml: proto_types.InvalidVarsYAML = betterproto.message_field(
        108, group="detail"
    )
    dbt_project_error: proto_types.DbtProjectError = betterproto.message_field(
        109, group="detail"
    )
    dbt_project_error_exception: proto_types.DbtProjectErrorException = (
        betterproto.message_field(110, group="detail")
    )
    dbt_profile_error: proto_types.DbtProfileError = betterproto.message_field(
        111, group="detail"
    )
    dbt_profile_error_exception: proto_types.DbtProfileErrorException = (
        betterproto.message_field(112, group="detail")
    )
    profile_list_title: proto_types.ProfileListTitle = betterproto.message_field(
        113, group="detail"
    )
    list_single_profile: proto_types.ListSingleProfile = betterproto.message_field(
        114, group="detail"
    )
    no_defined_profiles: proto_types.NoDefinedProfiles = betterproto.message_field(
        115, group="detail"
    )
    profile_help_message: proto_types.ProfileHelpMessage = betterproto.message_field(
        116, group="detail"
    )
    starter_project_path: proto_types.StarterProjectPath = betterproto.message_field(
        117, group="detail"
    )
    config_folder_directory: proto_types.ConfigFolderDirectory = (
        betterproto.message_field(118, group="detail")
    )
    no_sample_profile_found: proto_types.NoSampleProfileFound = (
        betterproto.message_field(119, group="detail")
    )
    profile_written_with_sample: proto_types.ProfileWrittenWithSample = (
        betterproto.message_field(120, group="detail")
    )
    profile_written_with_target_template_yaml: proto_types.ProfileWrittenWithTargetTemplateYAML = betterproto.message_field(
        121, group="detail"
    )
    profile_written_with_project_template_yaml: proto_types.ProfileWrittenWithProjectTemplateYAML = betterproto.message_field(
        122, group="detail"
    )
    setting_up_profile: proto_types.SettingUpProfile = betterproto.message_field(
        123, group="detail"
    )
    invalid_profile_template_yaml: proto_types.InvalidProfileTemplateYAML = (
        betterproto.message_field(124, group="detail")
    )
    project_name_already_exists: proto_types.ProjectNameAlreadyExists = (
        betterproto.message_field(125, group="detail")
    )
    project_created: proto_types.ProjectCreated = betterproto.message_field(
        126, group="detail"
    )
    package_redirect_deprecation: proto_types.PackageRedirectDeprecation = (
        betterproto.message_field(201, group="detail")
    )
    package_install_path_deprecation: proto_types.PackageInstallPathDeprecation = (
        betterproto.message_field(202, group="detail")
    )
    config_source_path_deprecation: proto_types.ConfigSourcePathDeprecation = (
        betterproto.message_field(203, group="detail")
    )
    config_data_path_deprecation: proto_types.ConfigDataPathDeprecation = (
        betterproto.message_field(204, group="detail")
    )
    adapter_deprecation_warning: proto_types.AdapterDeprecationWarning = (
        betterproto.message_field(205, group="detail")
    )
    metric_attributes_renamed: proto_types.MetricAttributesRenamed = (
        betterproto.message_field(206, group="detail")
    )
    exposure_name_deprecation: proto_types.ExposureNameDeprecation = (
        betterproto.message_field(207, group="detail")
    )
    adapter_event_debug: proto_types.AdapterEventDebug = betterproto.message_field(
        301, group="detail"
    )
    adapter_event_info: proto_types.AdapterEventInfo = betterproto.message_field(
        302, group="detail"
    )
    adapter_event_warning: proto_types.AdapterEventWarning = betterproto.message_field(
        303, group="detail"
    )
    adapter_event_error: proto_types.AdapterEventError = betterproto.message_field(
        304, group="detail"
    )
    new_connection: proto_types.NewConnection = betterproto.message_field(
        305, group="detail"
    )
    connection_reused: proto_types.ConnectionReused = betterproto.message_field(
        306, group="detail"
    )
    connection_left_open_in_cleanup: proto_types.ConnectionLeftOpenInCleanup = (
        betterproto.message_field(307, group="detail")
    )
    connection_closed_in_cleanup: proto_types.ConnectionClosedInCleanup = (
        betterproto.message_field(308, group="detail")
    )
    rollback_failed: proto_types.RollbackFailed = betterproto.message_field(
        309, group="detail"
    )
    connection_closed: proto_types.ConnectionClosed = betterproto.message_field(
        310, group="detail"
    )
    connection_left_open: proto_types.ConnectionLeftOpen = betterproto.message_field(
        311, group="detail"
    )
    rollback: proto_types.Rollback = betterproto.message_field(312, group="detail")
    cache_miss: proto_types.CacheMiss = betterproto.message_field(313, group="detail")
    list_relations: proto_types.ListRelations = betterproto.message_field(
        314, group="detail"
    )
    connection_used: proto_types.ConnectionUsed = betterproto.message_field(
        315, group="detail"
    )
    sql_query: proto_types.SQLQuery = betterproto.message_field(316, group="detail")
    sql_query_status: proto_types.SQLQueryStatus = betterproto.message_field(
        317, group="detail"
    )
    sql_commit: proto_types.SQLCommit = betterproto.message_field(318, group="detail")
    col_type_change: proto_types.ColTypeChange = betterproto.message_field(
        319, group="detail"
    )
    schema_creation: proto_types.SchemaCreation = betterproto.message_field(
        320, group="detail"
    )
    schema_drop: proto_types.SchemaDrop = betterproto.message_field(321, group="detail")
    uncached_relation: proto_types.UncachedRelation = betterproto.message_field(
        322, group="detail"
    )
    add_link: proto_types.AddLink = betterproto.message_field(323, group="detail")
    add_relation: proto_types.AddRelation = betterproto.message_field(
        324, group="detail"
    )
    drop_missing_relation: proto_types.DropMissingRelation = betterproto.message_field(
        325, group="detail"
    )
    drop_cascade: proto_types.DropCascade = betterproto.message_field(
        326, group="detail"
    )
    drop_relation: proto_types.DropRelation = betterproto.message_field(
        327, group="detail"
    )
    update_reference: proto_types.UpdateReference = betterproto.message_field(
        328, group="detail"
    )
    temporary_relation: proto_types.TemporaryRelation = betterproto.message_field(
        329, group="detail"
    )
    rename_schema: proto_types.RenameSchema = betterproto.message_field(
        330, group="detail"
    )
    dump_before_add_graph: proto_types.DumpBeforeAddGraph = betterproto.message_field(
        331, group="detail"
    )
    dump_after_add_graph: proto_types.DumpAfterAddGraph = betterproto.message_field(
        332, group="detail"
    )
    dump_before_rename_schema: proto_types.DumpBeforeRenameSchema = (
        betterproto.message_field(333, group="detail")
    )
    dump_after_rename_schema: proto_types.DumpAfterRenameSchema = (
        betterproto.message_field(334, group="detail")
    )
    adapter_import_error: proto_types.AdapterImportError = betterproto.message_field(
        335, group="detail"
    )
    plugin_load_error: proto_types.PluginLoadError = betterproto.message_field(
        336, group="detail"
    )
    new_connection_opening: proto_types.NewConnectionOpening = (
        betterproto.message_field(337, group="detail")
    )
    code_execution: proto_types.CodeExecution = betterproto.message_field(
        338, group="detail"
    )
    code_execution_status: proto_types.CodeExecutionStatus = betterproto.message_field(
        339, group="detail"
    )
    catalog_generation_error: proto_types.CatalogGenerationError = (
        betterproto.message_field(340, group="detail")
    )
    write_catalog_failure: proto_types.WriteCatalogFailure = betterproto.message_field(
        341, group="detail"
    )
    catalog_written: proto_types.CatalogWritten = betterproto.message_field(
        342, group="detail"
    )
    cannot_generate_docs: proto_types.CannotGenerateDocs = betterproto.message_field(
        343, group="detail"
    )
    building_catalog: proto_types.BuildingCatalog = betterproto.message_field(
        344, group="detail"
    )
    database_error_running_hook: proto_types.DatabaseErrorRunningHook = (
        betterproto.message_field(345, group="detail")
    )
    hooks_running: proto_types.HooksRunning = betterproto.message_field(
        346, group="detail"
    )
    hook_finished: proto_types.HookFinished = betterproto.message_field(
        347, group="detail"
    )
    parse_cmd_start: proto_types.ParseCmdStart = betterproto.message_field(
        401, group="detail"
    )
    parse_cmd_compiling: proto_types.ParseCmdCompiling = betterproto.message_field(
        402, group="detail"
    )
    parse_cmd_writing_manifest: proto_types.ParseCmdWritingManifest = (
        betterproto.message_field(403, group="detail")
    )
    parse_cmd_done: proto_types.ParseCmdDone = betterproto.message_field(
        404, group="detail"
    )
    manifest_dependencies_loaded: proto_types.ManifestDependenciesLoaded = (
        betterproto.message_field(405, group="detail")
    )
    manifest_lader_created: proto_types.ManifestLoaderCreated = (
        betterproto.message_field(406, group="detail")
    )
    manifest_loaded: proto_types.ManifestLoaded = betterproto.message_field(
        407, group="detail"
    )
    manifest_checked: proto_types.ManifestChecked = betterproto.message_field(
        408, group="detail"
    )
    manifest_flat_graph_built: proto_types.ManifestFlatGraphBuilt = (
        betterproto.message_field(409, group="detail")
    )
    parse_cmd_perf_info_path: proto_types.ParseCmdPerfInfoPath = (
        betterproto.message_field(410, group="detail")
    )
    generic_test_file_parse: proto_types.GenericTestFileParse = (
        betterproto.message_field(411, group="detail")
    )
    macro_file_parse: proto_types.MacroFileParse = betterproto.message_field(
        412, group="detail"
    )
    partial_parsing_full_reparse_because_of_error: proto_types.PartialParsingFullReparseBecauseOfError = betterproto.message_field(
        413, group="detail"
    )
    partial_parsing_exception_file: proto_types.PartialParsingExceptionFile = (
        betterproto.message_field(414, group="detail")
    )
    partial_parsing_file: proto_types.PartialParsingFile = betterproto.message_field(
        415, group="detail"
    )
    partial_parsing_exception: proto_types.PartialParsingException = (
        betterproto.message_field(416, group="detail")
    )
    partial_parsing_skip_parsing: proto_types.PartialParsingSkipParsing = (
        betterproto.message_field(417, group="detail")
    )
    partial_parsing_macro_change_start_full_parse: proto_types.PartialParsingMacroChangeStartFullParse = betterproto.message_field(
        418, group="detail"
    )
    partial_parsing_project_env_vars_changed: proto_types.PartialParsingProjectEnvVarsChanged = betterproto.message_field(
        419, group="detail"
    )
    partial_parsing_profile_env_vars_changed: proto_types.PartialParsingProfileEnvVarsChanged = betterproto.message_field(
        420, group="detail"
    )
    partial_parsing_deleted_metric: proto_types.PartialParsingDeletedMetric = (
        betterproto.message_field(421, group="detail")
    )
    manifest_wrong_metadata_version: proto_types.ManifestWrongMetadataVersion = (
        betterproto.message_field(422, group="detail")
    )
    partial_parsing_version_mismatch: proto_types.PartialParsingVersionMismatch = (
        betterproto.message_field(423, group="detail")
    )
    partial_parsing_failed_because_config_change: proto_types.PartialParsingFailedBecauseConfigChange = betterproto.message_field(
        424, group="detail"
    )
    partial_parsing_failed_because_profile_change: proto_types.PartialParsingFailedBecauseProfileChange = betterproto.message_field(
        425, group="detail"
    )
    partial_parsing_failed_because_new_project_dependency: proto_types.PartialParsingFailedBecauseNewProjectDependency = betterproto.message_field(
        426, group="detail"
    )
    partial_parsing_failed_because_hash_changed: proto_types.PartialParsingFailedBecauseHashChanged = betterproto.message_field(
        427, group="detail"
    )
    partial_parsing_not_enabled: proto_types.PartialParsingNotEnabled = (
        betterproto.message_field(428, group="detail")
    )
    parsed_file_load_failed: proto_types.ParsedFileLoadFailed = (
        betterproto.message_field(429, group="detail")
    )
    partial_parsing_save_file_not_found: proto_types.PartialParseSaveFileNotFound = (
        betterproto.message_field(430, group="detail")
    )
    static_parser_caused_jinja_rendering: proto_types.StaticParserCausedJinjaRendering = betterproto.message_field(
        431, group="detail"
    )
    using_experimental_parser: proto_types.UsingExperimentalParser = (
        betterproto.message_field(432, group="detail")
    )
    sample_full_jinja_rendering: proto_types.SampleFullJinjaRendering = (
        betterproto.message_field(433, group="detail")
    )
    static_parser_fallback_jinja_rendering: proto_types.StaticParserFallbackJinjaRendering = betterproto.message_field(
        434, group="detail"
    )
    static_parsing_macro_override_detected: proto_types.StaticParsingMacroOverrideDetected = betterproto.message_field(
        435, group="detail"
    )
    static_parser_success: proto_types.StaticParserSuccess = betterproto.message_field(
        436, group="detail"
    )
    static_parser_failure: proto_types.StaticParserFailure = betterproto.message_field(
        437, group="detail"
    )
    experimental_parser_success: proto_types.ExperimentalParserSuccess = (
        betterproto.message_field(438, group="detail")
    )
    experimental_parser_failure: proto_types.ExperimentalParserFailure = (
        betterproto.message_field(439, group="detail")
    )
    partial_parsing_enabled: proto_types.PartialParsingEnabled = (
        betterproto.message_field(440, group="detail")
    )
    partial_parsing_added_file: proto_types.PartialParsingAddedFile = (
        betterproto.message_field(441, group="detail")
    )
    partial_parsing_deleted_file: proto_types.PartialParsingDeletedFile = (
        betterproto.message_field(442, group="detail")
    )
    partial_parsing_updated_file: proto_types.PartialParsingUpdatedFile = (
        betterproto.message_field(443, group="detail")
    )
    partial_parsing_node_missing_in_source_file: proto_types.PartialParsingNodeMissingInSourceFile = betterproto.message_field(
        444, group="detail"
    )
    partial_parsing_missing_nodes: proto_types.PartialParsingMissingNodes = (
        betterproto.message_field(445, group="detail")
    )
    partial_parsing_child_map_missing_unique_id: proto_types.PartialParsingChildMapMissingUniqueID = betterproto.message_field(
        446, group="detail"
    )
    partial_parsing_update_schema_file: proto_types.PartialParsingUpdateSchemaFile = (
        betterproto.message_field(447, group="detail")
    )
    partial_parsing_deleted_source: proto_types.PartialParsingDeletedSource = (
        betterproto.message_field(448, group="detail")
    )
    partial_parsing_deleted_exposure: proto_types.PartialParsingDeletedExposure = (
        betterproto.message_field(449, group="detail")
    )
    invalid_disabled_target_in_test_node: proto_types.InvalidDisabledTargetInTestNode = betterproto.message_field(
        450, group="detail"
    )
    unused_resource_config_path: proto_types.UnusedResourceConfigPath = (
        betterproto.message_field(451, group="detail")
    )
    seed_increased: proto_types.SeedIncreased = betterproto.message_field(
        452, group="detail"
    )
    seed_exceeds_limit_same_path: proto_types.SeedExceedsLimitSamePath = (
        betterproto.message_field(453, group="detail")
    )
    seed_exceeds_limit_and_path_changed: proto_types.SeedExceedsLimitAndPathChanged = (
        betterproto.message_field(454, group="detail")
    )
    seed_exceeds_limit_checksum_changed: proto_types.SeedExceedsLimitChecksumChanged = (
        betterproto.message_field(455, group="detail")
    )
    unused_tables: proto_types.UnusedTables = betterproto.message_field(
        456, group="detail"
    )
    wrong_resource_schema_file: proto_types.WrongResourceSchemaFile = (
        betterproto.message_field(457, group="detail")
    )
    no_node_for_yaml_key: proto_types.NoNodeForYamlKey = betterproto.message_field(
        458, group="detail"
    )
    macro_patch_not_found: proto_types.MacroPatchNotFound = betterproto.message_field(
        459, group="detail"
    )
    node_not_found_or_disabled: proto_types.NodeNotFoundOrDisabled = (
        betterproto.message_field(460, group="detail")
    )
    general_macro_warning: proto_types.GeneralMacroWarning = betterproto.message_field(
        461, group="detail"
    )
    git_sparse_checkout_subdirectory: proto_types.GitSparseCheckoutSubdirectory = (
        betterproto.message_field(501, group="detail")
    )
    git_progress_checkout_revision: proto_types.GitProgressCheckoutRevision = (
        betterproto.message_field(502, group="detail")
    )
    git_progress_updating_existing_dependency: proto_types.GitProgressUpdatingExistingDependency = betterproto.message_field(
        503, group="detail"
    )
    git_progress_pulling_new_dependency: proto_types.GitProgressPullingNewDependency = (
        betterproto.message_field(504, group="detail")
    )
    git_nothing_to_do: proto_types.GitNothingToDo = betterproto.message_field(
        505, group="detail"
    )
    git_progress_updated_checkout_range: proto_types.GitProgressUpdatedCheckoutRange = (
        betterproto.message_field(506, group="detail")
    )
    git_progress_checked_out_at: proto_types.GitProgressCheckedOutAt = (
        betterproto.message_field(507, group="detail")
    )
    registry_progress_get_request: proto_types.RegistryProgressGETRequest = (
        betterproto.message_field(508, group="detail")
    )
    registry_progress_get_response: proto_types.RegistryProgressGETResponse = (
        betterproto.message_field(509, group="detail")
    )
    selector_report_invalid_selector: proto_types.SelectorReportInvalidSelector = (
        betterproto.message_field(510, group="detail")
    )
    jinja_log_info: proto_types.JinjaLogInfo = betterproto.message_field(
        511, group="detail"
    )
    jinja_log_debug: proto_types.JinjaLogDebug = betterproto.message_field(
        512, group="detail"
    )
    deps_no_packages_found: proto_types.DepsNoPackagesFound = betterproto.message_field(
        513, group="detail"
    )
    deps_start_package_install: proto_types.DepsStartPackageInstall = (
        betterproto.message_field(514, group="detail")
    )
    deps_install_info: proto_types.DepsInstallInfo = betterproto.message_field(
        515, group="detail"
    )
    deps_update_available: proto_types.DepsUpdateAvailable = betterproto.message_field(
        516, group="detail"
    )
    deps_up_to_date: proto_types.DepsUpToDate = betterproto.message_field(
        517, group="detail"
    )
    deps_list_subdirectory: proto_types.DepsListSubdirectory = (
        betterproto.message_field(518, group="detail")
    )
    deps_notify_updates_available: proto_types.DepsNotifyUpdatesAvailable = (
        betterproto.message_field(519, group="detail")
    )
    retry_external_call: proto_types.RetryExternalCall = betterproto.message_field(
        520, group="detail"
    )
    record_retry_exception: proto_types.RecordRetryException = (
        betterproto.message_field(521, group="detail")
    )
    registry_index_progress_get_request: proto_types.RegistryIndexProgressGETRequest = (
        betterproto.message_field(522, group="detail")
    )
    registry_index_progress_get_response: proto_types.RegistryIndexProgressGETResponse = betterproto.message_field(
        523, group="detail"
    )
    registry_response_unexpected_type: proto_types.RegistryResponseUnexpectedType = (
        betterproto.message_field(524, group="detail")
    )
    registry_response_missing_top_keys: proto_types.RegistryResponseMissingTopKeys = (
        betterproto.message_field(525, group="detail")
    )
    registry_response_missing_nested_keys: proto_types.RegistryResponseMissingNestedKeys = betterproto.message_field(
        526, group="detail"
    )
    registry_response_extra_nested_keys: proto_types.RegistryResponseExtraNestedKeys = (
        betterproto.message_field(527, group="detail")
    )
    deps_set_download_directory: proto_types.DepsSetDownloadDirectory = (
        betterproto.message_field(528, group="detail")
    )
    deps_unpinned: proto_types.DepsUnpinned = betterproto.message_field(
        529, group="detail"
    )
    no_nodes_for_selection_criteria: proto_types.NoNodesForSelectionCriteria = (
        betterproto.message_field(530, group="detail")
    )
    running_operation_caught_error: proto_types.RunningOperationCaughtError = (
        betterproto.message_field(601, group="detail")
    )
    compile_complete: proto_types.CompileComplete = betterproto.message_field(
        602, group="detail"
    )
    freshness_check_complete: proto_types.FreshnessCheckComplete = (
        betterproto.message_field(603, group="detail")
    )
    seed_header: proto_types.SeedHeader = betterproto.message_field(604, group="detail")
    seed_header_separator: proto_types.SeedHeaderSeparator = betterproto.message_field(
        605, group="detail"
    )
    sql_runner_exception: proto_types.SQLRunnerException = betterproto.message_field(
        606, group="detail"
    )
    log_test_result: proto_types.LogTestResult = betterproto.message_field(
        607, group="detail"
    )
    log_start_line: proto_types.LogStartLine = betterproto.message_field(
        608, group="detail"
    )
    log_model_result: proto_types.LogModelResult = betterproto.message_field(
        609, group="detail"
    )
    log_snapshot_result: proto_types.LogSnapshotResult = betterproto.message_field(
        615, group="detail"
    )
    log_seed_result: proto_types.LogSeedResult = betterproto.message_field(
        616, group="detail"
    )
    log_freshness_result: proto_types.LogFreshnessResult = betterproto.message_field(
        617, group="detail"
    )
    log_cancel_line: proto_types.LogCancelLine = betterproto.message_field(
        622, group="detail"
    )
    default_selector: proto_types.DefaultSelector = betterproto.message_field(
        623, group="detail"
    )
    node_start: proto_types.NodeStart = betterproto.message_field(624, group="detail")
    node_finished: proto_types.NodeFinished = betterproto.message_field(
        625, group="detail"
    )
    query_cancelation_unsupported: proto_types.QueryCancelationUnsupported = (
        betterproto.message_field(626, group="detail")
    )
    concurrency_line: proto_types.ConcurrencyLine = betterproto.message_field(
        627, group="detail"
    )
    compiling_node: proto_types.CompilingNode = betterproto.message_field(
        628, group="detail"
    )
    writing_injected_sql_for_node: proto_types.WritingInjectedSQLForNode = (
        betterproto.message_field(629, group="detail")
    )
    node_compiling: proto_types.NodeCompiling = betterproto.message_field(
        630, group="detail"
    )
    node_executing: proto_types.NodeExecuting = betterproto.message_field(
        631, group="detail"
    )
    log_hook_start_line: proto_types.LogHookStartLine = betterproto.message_field(
        632, group="detail"
    )
    log_hook_end_line: proto_types.LogHookEndLine = betterproto.message_field(
        633, group="detail"
    )
    skipping_details: proto_types.SkippingDetails = betterproto.message_field(
        634, group="detail"
    )
    nothing_to_do: proto_types.NothingToDo = betterproto.message_field(
        635, group="detail"
    )
    running_operation_uncaught_error: proto_types.RunningOperationUncaughtError = (
        betterproto.message_field(636, group="detail")
    )
    end_run_result: proto_types.EndRunResult = betterproto.message_field(
        637, group="detail"
    )
    no_nodes_selected: proto_types.NoNodesSelected = betterproto.message_field(
        638, group="detail"
    )
    catchable_exception_on_run: proto_types.CatchableExceptionOnRun = (
        betterproto.message_field(702, group="detail")
    )
    internal_exception_on_run: proto_types.InternalExceptionOnRun = (
        betterproto.message_field(703, group="detail")
    )
    generic_exception_on_run: proto_types.GenericExceptionOnRun = (
        betterproto.message_field(704, group="detail")
    )
    node_connection_release_error: proto_types.NodeConnectionReleaseError = (
        betterproto.message_field(705, group="detail")
    )
    found_stats: proto_types.FoundStats = betterproto.message_field(706, group="detail")
    main_keyboard_interrupt: proto_types.MainKeyboardInterrupt = (
        betterproto.message_field(801, group="detail")
    )
    main_encountered_error: proto_types.MainEncounteredError = (
        betterproto.message_field(802, group="detail")
    )
    main_stack_trace: proto_types.MainStackTrace = betterproto.message_field(
        803, group="detail"
    )
    system_error_retrieving_mod_time: proto_types.SystemErrorRetrievingModTime = (
        betterproto.message_field(804, group="detail")
    )
    system_could_not_write: proto_types.SystemCouldNotWrite = betterproto.message_field(
        805, group="detail"
    )
    system_executing_cmd: proto_types.SystemExecutingCmd = betterproto.message_field(
        806, group="detail"
    )
    system_std_out_msg: proto_types.SystemStdOutMsg = betterproto.message_field(
        807, group="detail"
    )
    system_std_err_msg: proto_types.SystemStdErrMsg = betterproto.message_field(
        808, group="detail"
    )
    system_report_return_code: proto_types.SystemReportReturnCode = (
        betterproto.message_field(809, group="detail")
    )
    timing_info_collected: proto_types.TimingInfoCollected = betterproto.message_field(
        810, group="detail"
    )
    log_debug_stack_trace: proto_types.LogDebugStackTrace = betterproto.message_field(
        811, group="detail"
    )
    check_clean_path: proto_types.CheckCleanPath = betterproto.message_field(
        812, group="detail"
    )
    confirm_clean_path: proto_types.ConfirmCleanPath = betterproto.message_field(
        813, group="detail"
    )
    protected_clean_path: proto_types.ProtectedCleanPath = betterproto.message_field(
        814, group="detail"
    )
    finished_clean_path: proto_types.FinishedCleanPaths = betterproto.message_field(
        815, group="detail"
    )
    open_command: proto_types.OpenCommand = betterproto.message_field(
        816, group="detail"
    )
    empty_line: proto_types.EmptyLine = betterproto.message_field(817, group="detail")
    serving_docs_port: proto_types.ServingDocsPort = betterproto.message_field(
        818, group="detail"
    )
    serving_docs_access_info: proto_types.ServingDocsAccessInfo = (
        betterproto.message_field(819, group="detail")
    )
    serving_docs_exit_info: proto_types.ServingDocsExitInfo = betterproto.message_field(
        820, group="detail"
    )
    run_result_warning: proto_types.RunResultWarning = betterproto.message_field(
        821, group="detail"
    )
    run_result_failure: proto_types.RunResultFailure = betterproto.message_field(
        822, group="detail"
    )
    stats_line: proto_types.StatsLine = betterproto.message_field(823, group="detail")
    run_result_error: proto_types.RunResultError = betterproto.message_field(
        824, group="detail"
    )
    run_result_error_no_message: proto_types.RunResultErrorNoMessage = (
        betterproto.message_field(825, group="detail")
    )
    sql_compiled_path: proto_types.SQLCompiledPath = betterproto.message_field(
        826, group="detail"
    )
    check_node_test_failure: proto_types.CheckNodeTestFailure = (
        betterproto.message_field(827, group="detail")
    )
    first_run_result_error: proto_types.FirstRunResultError = betterproto.message_field(
        828, group="detail"
    )
    after_first_run_result_error: proto_types.AfterFirstRunResultError = (
        betterproto.message_field(829, group="detail")
    )
    end_of_run_summary: proto_types.EndOfRunSummary = betterproto.message_field(
        830, group="detail"
    )
    log_skip_because_error: proto_types.LogSkipBecauseError = betterproto.message_field(
        834, group="detail"
    )
    ensure_git_installed: proto_types.EnsureGitInstalled = betterproto.message_field(
        836, group="detail"
    )
    deps_creating_local_symlink: proto_types.DepsCreatingLocalSymlink = (
        betterproto.message_field(837, group="detail")
    )
    deps_symlink_not_available: proto_types.DepsSymlinkNotAvailable = (
        betterproto.message_field(838, group="detail")
    )
    disable_tracking: proto_types.DisableTracking = betterproto.message_field(
        839, group="detail"
    )
    sending_event: proto_types.SendingEvent = betterproto.message_field(
        840, group="detail"
    )
    send_event_failure: proto_types.SendEventFailure = betterproto.message_field(
        841, group="detail"
    )
    flush_events: proto_types.FlushEvents = betterproto.message_field(
        842, group="detail"
    )
    flush_events_failure: proto_types.FlushEventsFailure = betterproto.message_field(
        843, group="detail"
    )
    tracking_initialize_failure: proto_types.TrackingInitializeFailure = (
        betterproto.message_field(844, group="detail")
    )
    event_buffer_full: proto_types.EventBufferFull = betterproto.message_field(
        845, group="detail"
    )
    run_result_warning_message: proto_types.RunResultWarningMessage = (
        betterproto.message_field(846, group="detail")
    )
    integration_test_info: proto_types.IntegrationTestInfo = betterproto.message_field(
        901, group="detail"
    )
    integration_test_debug: proto_types.IntegrationTestDebug = (
        betterproto.message_field(902, group="detail")
    )
    integration_test_warn: proto_types.IntegrationTestWarn = betterproto.message_field(
        903, group="detail"
    )
    integration_test_error: proto_types.IntegrationTestError = (
        betterproto.message_field(904, group="detail")
    )
    integration_test_exception: proto_types.IntegrationTestException = (
        betterproto.message_field(905, group="detail")
    )
    unit_test_info: proto_types.UnitTestInfo = betterproto.message_field(
        906, group="detail"
    )
