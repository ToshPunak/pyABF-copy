# 18702001-pulseTrain.abf

## ABF Class Methods

* abf.baseline()
* abf.getInfoPage()
* abf.setSweep()
* abf.sweepAverage()
* abf.sweepD()
* abf.sweepError()

## ABF Class Variables

* abfDateTime = `2018-07-02 09:29:48`
* abfFileComment = ``
* abfFileFormat = `2`
* abfFilePath = `c:\Users\scott\Documents\GitHub\pyABF\data\abfs\18702001-pulseTrain.abf`
* abfID = `18702001-pulseTrain`
* abfVersion = `2.6.0.0`
* adcNames = `['IN 0', 'IN 1']`
* adcUnits = `['pA', 'A']`
* baselinePoints = `False`
* baselineTimes = `False`
* channelCount = `2`
* channelList = `[0, 1]`
* dacNames = `['Cmd 0', 'Cmd 1']`
* dacUnits = `['mV', 'mV']`
* data = `[[-11.71874905 -10.13183498  -9.03320217 ...,  -8.42285061  -8.05663967    -9.2773428 ]  [ -1.03607178  -1.03515625  -1.03546143 ...,  -1.03515625  -1.03515625    -1.03485107]]`
* dataByteStart = `6656`
* dataPointByteSize = `2`
* dataPointCount = `120000`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* digitalWaveformEpochs = `[[0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]]`
* epochPoints = `[312, 4312, 8312, 9312, 10312, 11312, 15312, 25312]`
* epochValues = `[[-80. -70. -80. -70. -20. -10.  25.]  [-80. -70. -80. -70. -20. -10.  35.]  [-80. -70. -80. -70. -20. -10.  45.]]`
* epochsByChannel = `[ChannelEpochs(ABF, 0), ChannelEpochs(ABF, 1)]`
* holdingCommand = `[-70.0, -10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* protocol = `0201 memtest`
* protocolPath = `\\Spike\locked\Protocols\permanent\0201 memtest.pro`
* sweepC = `[-70. -70. -70. ..., -70. -70. -70.]`
* sweepChannel = `0`
* sweepCount = `3`
* sweepLabelC = `Membrane Potential (mV)`
* sweepLabelX = `time (seconds)`
* sweepLabelY = `Clamp Current (pA)`
* sweepLengthSec = `1.0`
* sweepList = `[0, 1, 2]`
* sweepNumber = `0`
* sweepPointCount = `20000`
* sweepUnitsC = `mV`
* sweepUnitsX = `sec`
* sweepUnitsY = `pA`
* sweepX = `[  0.00000000e+00   5.00000000e-05   1.00000000e-04 ...,   9.99850000e-01    9.99900000e-01   9.99950000e-01]`
* sweepY = `[-11.71874905 -10.13183498  -9.03320217 ..., -15.01464748 -13.1835928  -11.35253811]`
* tagComments = `[]`
* tagSweeps = `[]`
* tagTimesMin = `[]`
* tagTimesSec = `[]`

## Epochs for Channel 0


```
                Ch0 EPOCH      A      B      C      D
                     Type   Step   Step   Ramp   Ramp
         First Level (mV)    -80    -70    -80    -70
         Delta Level (mV)      0      0      0      0
 First Duration (samples)   4000   4000   1000   1000
 Delta Duration (samples)      0      0      0      0
   Train Period (samples)      0      0      0      0
    Pulse Width (samples)      0      0      0      0
```

## Epochs for Channel 1


```
                Ch1 EPOCH      A      B      C
                     Type   Step   Step  Pulse
         First Level (mV)    -20    -10     25
         Delta Level (mV)      0      0     10
 First Duration (samples)   1000   4000  10000
 Delta Duration (samples)      0      0      0
   Train Period (samples)      0      0   1000
    Pulse Width (samples)      0      0    200
```

## ABF2 Header

> The first several bytes of an ABF2 file contain variables     located at specific byte positions from the start of the file. 

* FileGUID = `1160535393`
* fFileSignature = `ABF2`
* fFileVersionNumber = `[0, 0, 6, 2]`
* lActualEpisodes = `3`
* nCRCEnable = `0`
* nDataFormat = `0`
* nFileType = `1`
* nSimultaneousScan = `1`
* uCreatorNameIndex = `1`
* uCreatorVersion = `168230915`
* uFileCRC = `0`
* uFileInfoSize = `512`
* uFileStartDate = `20180702`
* uFileStartTimeMS = `34187630`
* uModifierNameIndex = `0`
* uModifierVersion = `0`
* uProtocolPathIndex = `2`
* uStopwatchTime = `1595`
* unknown1 = `1321524210`
* unknown2 = `1322714036`
* unknown3 = `1575391166`

## SectionMap

> Reading three numbers (int, int, long) at specific byte locations     yields the block position, byte size, and item count of specific     data stored in sections. Note that a block is 512 bytes. Some of     these sections are not read by this class because they are either     not useful for my applications, typically unused, or have an     unknown memory structure. 

* ADCPerDACSection = `[0, 0, 0]`
* ADCSection = `[2, 128, 2]`
* AnnotationSection = `[0, 0, 0]`
* DACSection = `[3, 256, 8]`
* DataSection = `[13, 2, 120000]`
* DeltaSection = `[0, 0, 0]`
* EpochPerDACSection = `[7, 48, 7]`
* EpochSection = `[8, 32, 4]`
* MathSection = `[0, 0, 0]`
* ProtocolSection = `[1, 512, 1]`
* ScopeSection = `[11, 769, 1]`
* StatsRegionSection = `[9, 128, 1]`
* StatsSection = `[0, 0, 0]`
* StringsSection = `[10, 191, 22]`
* SynchArraySection = `[482, 8, 3]`
* TagSection = `[0, 0, 0]`
* UserListSection = `[0, 0, 0]`
* VoiceTagSection = `[0, 0, 0]`

## ProtocolSection

> This section contains information about the recording settings.     This is useful for determining things like sample rate and     channel scaling factors. 

* bEnableFileCompression = `0`
* fADCRange = `10.0`
* fADCSequenceInterval = `50.0`
* fAverageWeighting = `0.10000000149011612`
* fCellID = `[0.0, 0.0, 0.0]`
* fDACRange = `10.0`
* fEpisodeStartToStart = `0.0`
* fFirstRunDelayS = `0.0`
* fRunStartToStart = `0.0`
* fScopeOutputInterval = `0.0`
* fSecondsPerRun = `7200.0`
* fStatisticsPeriod = `1.0`
* fSynchTimeUnit = `6.25`
* fTrialStartToStart = `0.0`
* fTriggerThreshold = `0.0`
* lADCResolution = `32768`
* lAverageCount = `1`
* lDACResolution = `32768`
* lEpisodesPerRun = `3`
* lFileCommentIndex = `0`
* lFinishDisplayNum = `12000`
* lNumSamplesPerEpisode = `40000`
* lNumberOfTrials = `1`
* lPreTriggerSamples = `40`
* lRunsPerTrial = `1`
* lSamplesPerTrace = `40000`
* lStartDisplayNum = `0`
* lStatisticsMeasurements = `5`
* lTimeHysteresis = `1`
* nActiveDACChannel = `0`
* nAllowExternalTags = `0`
* nAlternateDACOutputState = `0`
* nAlternateDigitalOutputState = `0`
* nAutoAnalyseEnable = `1`
* nAutoTriggerStrategy = `1`
* nAverageAlgorithm = `0`
* nAveragingMode = `0`
* nChannelStatsStrategy = `0`
* nCommentsEnable = `0`
* nDigitalDACChannel = `0`
* nDigitalEnable = `0`
* nDigitalHolding = `0`
* nDigitalInterEpisode = `0`
* nDigitalTrainActiveLogic = `1`
* nDigitizerADCs = `16`
* nDigitizerDACs = `4`
* nDigitizerSynchDigitalOuts = `8`
* nDigitizerTotalDigitalOuts = `16`
* nDigitizerType = `6`
* nExperimentType = `2`
* nExternalTagType = `2`
* nFirstEpisodeInRun = `0`
* nLTPType = `0`
* nLevelHysteresis = `64`
* nManualInfoStrategy = `1`
* nOperationMode = `5`
* nScopeTriggerOut = `0`
* nShowPNRawData = `0`
* nSignalType = `0`
* nStatisticsClearStrategy = `1`
* nStatisticsDisplayStrategy = `0`
* nStatisticsSaveStrategy = `0`
* nStatsEnable = `0`
* nTrialTriggerSource = `-1`
* nTriggerAction = `0`
* nTriggerPolarity = `0`
* nTriggerSource = `-3`
* nUndoPromptStrategy = `0`
* nUndoRunCount = `0`
* uFileCompressionRatio = `1`

## ADCSection

> Information about the ADC (what gets recorded).      There is 1 item per ADC. 

* bEnabledDuringPN = `[0, 0]`
* fADCDisplayAmplification = `[6.578846454620361, 1.0]`
* fADCDisplayOffset = `[4.0, 0.0]`
* fADCProgrammableGain = `[1.0, 1.0]`
* fInstrumentOffset = `[0.0, 0.0]`
* fInstrumentScaleFactor = `[0.0005000000237487257, 1.0]`
* fPostProcessLowpassFilter = `[100000.0, 100000.0]`
* fSignalGain = `[1.0, 1.0]`
* fSignalHighpassFilter = `[1.0, 1.0]`
* fSignalLowpassFilter = `[5000.0, 5000.0]`
* fSignalOffset = `[0.0, 0.0]`
* fTelegraphAccessResistance = `[0.0, 0.0]`
* fTelegraphAdditGain = `[5.0, 1.0]`
* fTelegraphFilter = `[2000.0, 1000.0]`
* fTelegraphMembraneCap = `[0.0, 0.0]`
* lADCChannelNameIndex = `[3, 5]`
* lADCUnitsIndex = `[4, 6]`
* nADCNum = `[0, 1]`
* nADCPtoLChannelMap = `[0, 1]`
* nADCSamplingSeq = `[0, 0]`
* nHighpassFilterType = `[0, 0]`
* nLowpassFilterType = `[0, 0]`
* nPostProcessLowpassFilterType = `['\x00', '\x00']`
* nStatsChannelPolarity = `[1, 0]`
* nTelegraphEnable = `[1, 0]`
* nTelegraphInstrument = `[24, 0]`
* nTelegraphMode = `[0, 0]`

## DACSection

> Information about the DAC (what gets clamped).      There is 1 item per DAC. 

* fBaselineDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fBaselineLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACCalibrationFactor = `[1.001173496246338, 1.0012290477752686, 1.001173496246338, 1.001173496246338, 1.0, 1.0, 1.0, 1.0]`
* fDACCalibrationOffset = `[-4.0, -4.0, -7.0, -6.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fDACHoldingLevel = `[-70.0, -10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACScaleFactor = `[20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]`
* fInstrumentHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fMembTestPostSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fMembTestPreSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPNHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNInterpulse = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNSettlingTime = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPostTrainLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPostTrainPeriod = `[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]`
* fStepDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fStepLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* lConditNumPulses = `[1, 0, 0, 0, 0, 0, 0, 0]`
* lDACChannelNameIndex = `[7, 9, 11, 13, 15, 17, 19, 21]`
* lDACChannelUnitsIndex = `[8, 10, 12, 14, 16, 18, 20, 22]`
* lDACFileEpisodeNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFileNumEpisodes = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePathIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePtr = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nConditEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACFileADCNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACNum = `[0, 1, 2, 3, 4, 5, 6, 7]`
* nInterEpisodeLevel = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPPresynapticPulses = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPUsageOfDAC = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractADCIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractType = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nMembTestEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumADCChannels = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumPulses = `[4, 4, 4, 4, 4, 4, 4, 4]`
* nPNPolarity = `[1, 1, 1, 1, 1, 1, 1, 1]`
* nPNPosition = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nTelegraphDACScaleFactorEnable = `[1, 0, 0, 0, 0, 0, 0, 0]`
* nWaveformEnable = `[1, 1, 0, 0, 0, 0, 0, 0]`
* nWaveformSource = `[1, 1, 1, 1, 0, 0, 0, 0]`

## EpochPerDACSection

> This section contains waveform protocol information. These are most of     the values set when using the epoch the waveform editor. Note that digital     output signals are not stored here, but are in EpochSection. 

* fEpochInitLevel = `[-80.0, -70.0, -80.0, -70.0, -20.0, -10.0, 25.0]`
* fEpochLevelInc = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.0]`
* lEpochDurationInc = `[0, 0, 0, 0, 0, 0, 0]`
* lEpochInitDuration = `[4000, 4000, 1000, 1000, 1000, 4000, 10000]`
* lEpochPulsePeriod = `[0, 0, 0, 0, 0, 0, 1000]`
* lEpochPulseWidth = `[0, 0, 0, 0, 0, 0, 200]`
* nDACNum = `[0, 0, 0, 0, 1, 1, 1]`
* nEpochNum = `[0, 1, 2, 3, 0, 1, 2]`
* nEpochType = `[1, 1, 2, 2, 1, 1, 3]`

## EpochSection

> This section contains the digital output signals for each epoch. This     section has been overlooked by some previous open-source ABF-reading     projects. Note that the digital output is a single byte, but represents      8 bits corresponding to 8 outputs (7->0). When working with these bits,     I convert it to a string like "10011101" for easy eyeballing. 

* nEpochDigitalOutput = `[0, 0, 0, 0]`
* nEpochNum = `[0, 1, 2, 3]`

## TagSection

> Tags are comments placed in ABF files during the recording. Physically     they are located at the end of the file (after the data).      Later we will populate the times and sweeps (human-understandable units)     by multiplying the lTagTime by fSynchTimeUnit from the protocol section. 

* lTagTime = `[]`
* nTagType = `[]`
* nVoiceTagNumberorAnnotationIndex = `[]`
* sComment = `[]`
* sweeps = `[]`
* timesMin = `[]`
* timesSec = `[]`

## StringsSection

> Part of the ABF file contains long strings. Some of these can be broken     apart into indexed strings.       The first string is the only one which seems to contain useful information.     This contains information like channel names, channel units, and abf      protocol path and comments. The other strings are very large and I do not      know what they do.      Strings which contain indexed substrings are separated by \x00 characters. 

* strings = `[b'SSCH\x01\x00\x00\x00\x16\x00\x00\x003\x00\x00\x00\x93\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Clampex\x00\\\\Spike\\locked\\Protocols\\permanent\\0201 memtest.pro\x00IN 0\x00pA\x00IN 1\x00A\x00Cmd 0\x00mV\x00Cmd 1\x00mV\x00Cmd 2\x00mV\x00Cmd 3\x00mV\x00AO #4\x00mV\x00AO #5\x00mV\x00AO #6\x00mV\x00AO #7\x00mV\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00@\x04\xff\xff\xff\x00\xc0\xc0\xc0\x00\x80\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\xc0\xc0\xc0\x00\xff\xff\x00\x00\x80\x80\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00@\x9cF\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\xf5\xff\x90\x01 \x00\x00\x00Arial\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00IN 0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x01\x00\x00\x00\x00\x00\x00?_\xff\x9fB\x00\x00\x00\xc1IN 1\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xff\x00\x01\x00\x00\x00\x00\x00\x00?$\xf2\xd8?hf\xe6?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00J\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x80\x00\x00\x80\x80\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x80\x80\x00\x80\x80\x80\x00\xff\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\xa0\xff\xbd\xf2\xad\xff\xc0\xf2\xb6\xff\xbf\xf2\xbc\xff\xbf\xf2\xbb\xff\xbf\xf2\xb2\xff\xbd\xf2\xa9\xff\xc0\xf2\xa1\xff\xbd\xf2\x9a\xff\xbf\xf2\x9a\xff\xbe\xf2\x9a\xff\xbe\xf2\x9e\xff\xbf\xf2\x9e\xff\xc1\xf2\x9a\xff\xc0\xf2\x94\xff\xc1\xf2\x90\xff\xc0\xf2\x90\xff\xc0\xf2\x93\xff\xc1\xf2\x9b\xff\xc0\xf2\x9f\xff\xbf\xf2\x99\xff\xbf\xf2\x95\xff\xbf\xf2\x9a\xff\xbe\xf2\x9e\xff\xbd\xf2\xa2\xff\xc0\xf2\xa4\xff\xc0\xf2\xa3\xff\xc2\xf2\x9d\xff\xc1\xf2\x95\xff\xc0\xf2\x90\xff\xbf\xf2\x92\xff\xbf\xf2\x94\xff\xbe\xf2\x99\xff\xbe\xf2\x9c\xff\xc0\xf2\x9e\xff\xbf\xf2\xa4\xff\xbf\xf2\xae\xff\xbe\xf2\xb0\xff\xbe\xf2\xa5\xff\xbf\xf2\x99\xff\xbf\xf2\x92\xff\xc1\xf2\x8d\xff\xc0\xf2\x8c\xff\xbf\xf2\x91\xff\xc0\xf2\x9d\xff\xc3\xf2\xa9\xff\xc3', b'\xf2\xab\xff\xc1\xf2\xa2\xff\xc1\xf2\x9a\xff\xc3\xf2\x91\xff\xc2\xf2\x92\xff\xc1\xf2\xa1\xff\xc1\xf2\xb0\xff\xc0\xf2\xb6\xff\xbe\xf2\xb3\xff\xbf\xf2\xad\xff\xbf\xf2\xaa\xff\xbf\xf2\xa1\xff\xc0\xf2\x9e\xff\xbf\xf2\xa2\xff\xbf\xf2\xa5\xff\xbd\xf2\x9f\xff\xbd\xf2\x98\xff\xbe\xf2\x97\xff\xbf\xf2\x98\xff\xbd\xf2\x9a\xff\xbf\xf2\x9d\xff\xbf\xf2\xa2\xff\xbf\xf2\xa2\xff\xbf\xf2\x9d\xff\xbf\xf2\x9c\xff\xbf\xf2\xa0\xff\xbf\xf2\xa0\xff\xbd\xf2\x9b\xff\xc0\xf2\x9a\xff\xc0\xf2\x9f\xff\xbe\xf2\xa2\xff\xbd\xf2\xa5\xff\xbd\xf2\xa9\xff\xbe\xf2\xad\xff\xc0\xf2\xb6\xff\xc3\xf2\xc2\xff\xc3\xf2\xc2\xff\xc0\xf2\xb8\xff\xbf\xf2\xa9\xff\xbf\xf2\x99\xff\xbe\xf2\x96\xff\xbe\xf2\x94\xff\xbd\xf2\x97\xff\xbb\xf2\x99\xff\xbd\xf2\x97\xff\xc0\xf2\x91\xff\xbf\xf2\x8e\xff\xbf\xf2\x91\xff', b'\xc2\xf2\x98\xff\xc0\xf2\x9f\xff\xbe\xf2\xa1\xff\xbe\xf2\xa2\xff\xc1\xf2\x9b\xff\xc0\xf2\x8c\xff\xbf\xf2\x81\xff\xbd\xf2}\xff\xc0\xf2\x82\xff\xbf\xf2\x90\xff\xbf\xf2\x9f\xff\xbd\xf2\xa9\xff\xbe\xf2\xaa\xff\xc1\xf2\xa4\xff\xc1\xf2\x9f\xff\xbd\xf2\xa1\xff\xbd\xf2\xa7\xff\xbe\xf2\xb1\xff\xbd\xf2\xbb\xff\xbe\xf2\xbf\xff\xbf\xf2\xb8\xff\xbe\xf2\xa6\xff\xbc\xf2\x98\xff\xbd\xf2\x95\xff\xbf\xf2\x95\xff\xbf\xf2\x98\xff\xbe\xf2\xa2\xff\xc0\xf2\xb1\xff\xbd\xf2\xba\xff\xbc\xf2\xbb\xff\xc0\xf2\xb3\xff\xc0\xf2\xab\xff\xbe\xf2\xa6\xff\xbe\xf2\x9e\xff\xc0\xf2\x92\xff\xbd\xf2\x87\xff\xbd\xf2\x89\xff\xbe\xf2\x95\xff\xc1\xf2\xa5\xff\xc0\xf2\xaa\xff\xbe\xf2\xa7\xff\xbd\xf2\xa2\xff\xba\xf2\x9d\xff\xbd\xf2\x97\xff\xba\xf2\x94\xff\xbb\xf2\x91\xff\xbd\xf2\x91\xff\xbd\xf2\x94', b'\xff\xbe\xf2\x9b\xff\xbc\xf2\xa2\xff\xbc\xf2\xa7\xff\xbb\xf2\xa5\xff\xbe\xf2\x9f\xff\xbf\xf2\x97\xff\xbf\xf2\x94\xff\xbd\xf2\x99\xff\xbd\xf2\xa8\xff\xbe\xf2\xb1\xff\xb8\xf2\xb6\xff\xb7\xf2\xb8\xff\xba\xf2\xb6\xff\xbe\xf2\xad\xff\xbd\xf2\x9c\xff\xbe\xf2\x8e\xff\xbb\xf2\x88\xff\xbd\xf2\x8c\xff\xbb\xf2\x96\xff\xba\xf2\x9f\xff\xbb\xf2\xa6\xff\xbd\xf2\xad\xff\xbd\xf2\xb4\xff\xbe\xf2\xb6\xff\xbd\xf2\xb5\xff\xbd\xf2\xae\xff\xbb\xf2\xa4\xff\xbc\xf2\x9f\xff\xbc\xf2\xa2\xff\xbb\xf2\xa9\xff\xbc\xf2\xaa\xff\xbc\xf2\xa9\xff\xbc\xf2\xa5\xff\xbe\xf2\x9e\xff\xbc\xf2\x9b\xff\xbd\xf2\x9c\xff\xbb\xf2\x9e\xff\xbb\xf2\xa6\xff\xbd\xf2\xb2\xff\xbd\xf2\xbe\xff\xbb\xf2\xc3\xff\xba\xf2\xba\xff\xbe\xf2\xaa\xff\xbd\xf2\x9d\xff\xbc\xf2\x95\xff\xbd\xf2\x91\xff\xbb\xf2\x91\xff\xbc\xf2', b'\x98\xff\xbd\xf2\x9d\xff\xbc\xf2\x9b\xff\xbd\xf2\x9a\xff\xba\xf2\xa5\xff\xbb\xf2\xb0\xff\xbb\xf2\xb1\xff\xbd\xf2\xa3\xff\xbe\xf2\x94\xff\xbf\xf2\x93\xff\xc0\xf2\x9f\xff\xbf\xf2\xa6\xff\xbd\xf2\xaa\xff\xbe\xf2\xa8\xff\xbd\xf2\xa4\xff\xbc\xf2\x9d\xff\xbb\xf2\x94\xff\xba\xf2\x92\xff\xbb\xf2\x8e\xff\xb9\xf2\x8b\xff\xbb\xf2\x8b\xff\xbb\xf2\x90\xff\xbb\xf2\x98\xff\xbb\xf2\xa1\xff\xba\xf2\xad\xff\xba\xf2\xae\xff\xba\xf2\xa8\xff\xba\xf2\xa2\xff\xba\xf2\xa1\xff\xbc\xf2\xa5\xff\xbe\xf2\xaa\xff\xbe\xf2\xb5\xff\xbf\xf2\xb8\xff\xbe\xf2\xaf\xff\xbd\xf2\xa1\xff\xbd\xf2\x98\xff\xbd\xf2\x97\xff\xbc\xf2\x9e\xff\xbe\xf2\xa5\xff\xbe\xf2\xb1\xff\xbd\xf2\xbd\xff\xbe\xf2\xc4\xff\xbf\xf2\xc1\xff\xbf\xf2\xb6\xff\xbd\xf2\xac\xff\xbe\xf2\xa6\xff\xbe\xf2\xa2\xff\xbd\xf2\x9b\xff\xbe', b'\xf2\x93\xff\xbd\xf2\x93\xff\xbd\xf2\x95\xff\xbe\xf2\x98\xff\xbf\xf2\x9f\xff\xbe\xf2\xa4\xff\xbd\xf2\xa9\xff\xbd\xf2\xa7\xff\xbe\xf2\xa5\xff\xbd\xf2\xa6\xff\xbc\xf2\xa5\xff\xb9\xf2\xa9\xff\xbb\xf2\xad\xff\xbd\xf2\xb2\xff\xbc\xf2\xae\xff\xbb\xf2\xa3\xff\xbc\xf2\x9e\xff\xbf\xf2\x9d\xff\xbf\xf2\x9a\xff\xbf\xf2\x96\xff\xbb\xf2\x99\xff\xbd\xf2\x98\xff\xbe\xf2\x90\xff\xb9\xf2\x8a\xff\xba\xf2\x8a\xff\xbc\xf2\x8b\xff\xbd\xf2\x8d\xff\xbd\xf2\x8f\xff\xbc\xf2\x8f\xff\xbe\xf2\x90\xff\xbe\xf2\x94\xff\xbd\xf2\x9c\xff\xbe\xf2\xa8\xff\xbe\xf2\xae\xff\xbf\xf2\xb2\xff\xbe\xf2\xb0\xff\xbd\xf2\xaa\xff\xba\xf2\xa1\xff\xbd\xf2\x99\xff\xbe\xf2\x96\xff\xbf\xf2\x98\xff\xbd\xf2\x9e\xff\xbc\xf2\xa1\xff\xbd\xf2\xa1\xff\xbe\xf2\x9f\xff\xc0\xf2\x9c\xff\xc0\xf2\x98\xff\xc0\xf2\x94\xff', b"\xbe\xf2\x98\xff\xbb\xf2\x9b\xff\xbf\xf2\xa5\xff\xbf\xf2\xac\xff\xbe\xf2\xaa\xff\xbe\xf2\xa5\xff\xbe\xf2\x9d\xff\xbe\xf2\x97\xff\xbb\xf2\x98\xff\xbf\xf2\x97\xff\xbf\xf2\x96\xff\xc0\xf2\x97\xff\xbf\xf2\x99\xff\xbd\xf2\x93\xff\xbb\xf2\x8c\xff\xbd\xf2\x8e\xff\xbf\xf2\x9c\xff\xc0\xf2\xae\xff\xc0\xf2\xb9\xff\xbf\xf2\xb9\xff\xbf\xf2\xae\xff\xbd\xf2\x9d\xff\xbc\xf2\x8f\xff\xbf\xf2\x94\xff\xbe\xf2\xa6\xff\xc0\xf2\xb7\xff\xc0\xf2\xbc\xff\xbf\xf2\xb4\xff\xbe\xf2x\xffE\xf2\x16\xfd8\xf2\x9a\xf7K\xf2\x8e\xf1J\xf2\x8d\xedD\xf2b\xec<\xf2^\xed2\xf2W\xef'\xf2}\xf1\x1c\xf2m\xf3\x12\xf2\x0e\xf5\n\xf2j\xf6\x03\xf2\x94\xf7\xfc\xf1\x94\xf8\xf2\xf1q\xf9\xe6\xf15\xfa\xdc\xf1\xdd\xfa\xd3\xf1p\xfb\xc9\xf1\xf6\xfb\xbf\xf1j", b'\xfc\xb8\xf1\xcd\xfc\xb0\xf1 \xfd\xa5\xf1l\xfd\x9e\xf1\xaf\xfd\x95\xf1\xe3\xfd\x8c\xf1\x07\xfe\x83\xf1\'\xfey\xf1C\xfen\xf1]\xfeg\xf1v\xfe_\xf1\x8a\xfeW\xf1\x97\xfeP\xf1\x9d\xfeE\xf1\xa5\xfe?\xf1\xb4\xfe6\xf1\xc0\xfe*\xf1\xc9\xfe$\xf1\xce\xfe\x1d\xf1\xd5\xfe\x11\xf1\xde\xfe\t\xf1\xec\xfe\xff\xf0\xf6\xfe\xf8\xf0\xf2\xfe\xee\xf0\xea\xfe\xe8\xf0\xe7\xfe\xdf\xf0\xe9\xfe\xd8\xf0\xf2\xfe\xcf\xf0\xf7\xfe\xc5\xf0\xf9\xfe\xbd\xf0\xf9\xfe\xb5\xf0\x01\xff\xab\xf0\x0e\xff\xa3\xf0\x18\xff\x99\xf0"\xff\x92\xf0!\xff\x8a\xf0\x1a\xff\x81\xf0\x0f\xff{\xf0\x06\xffs\xf0\x02\xffl\xf0\xff\xfed\xf0\x01\xff]\xf0\x02\xffU\xf0\x06\xffM\xf0\x07\xffD\xf0\x04\xff=\xf0\x01\xff5\xf0\x00\xff/\xf0', b'\x02\xff(\xf0\x04\xff\x1d\xf0\x04\xff\x15\xf0\x06\xff\r\xf0\xff\xfe\x04\xf0\xf4\xfe\xfa\xef\xec\xfe\xf3\xef\xeb\xfe\xec\xef\xf2\xfe\xe4\xef\xfb\xfe\xdc\xef\xfd\xfe\xd6\xef\xf7\xfe\xcc\xef\xf6\xfe\xc7\xef\x00\xff\xbf\xef\t\xff\xb7\xef\x11\xff\xae\xef\x14\xff\xa6\xef\x0f\xff\xa1\xef\x06\xff\x9a\xef\xfa\xfe\x93\xef\xf0\xfe\x8b\xef\xf1\xfe\x83\xef\xf9\xfez\xef\xfe\xfer\xef\x00\xffm\xef\xfd\xfee\xef\xfb\xfe^\xef\xfb\xfeU\xef\xf9\xfeN\xef\xfd\xfeH\xef\t\xff@\xef\x11\xff7\xef\x0e\xff5\xef\n\xff.\xef\x07\xff%\xef\x05\xff\x1e\xef\x03\xff\x16\xef\xfe\xfe\r\xef\xf9\xfe\x06\xef\xfa\xfe\x00\xef\xfa\xfe\xf8\xee\xf8\xfe\xf1\xee\xfa\xfe\xeb\xee\x01\xff\xe6\xee\x08\xff\xde\xee\t\xff\xd5\xee\t\xff\xd2\xee\x08\xff\xcb', b'\xee\x00\xff\xc2\xee\xfa\xfe\xb9\xee\xff\xfe\xb4\xee\x0b\xff\xad\xee\x0e\xff\xa5\xee\n\xff\x9f\xee\x05\xff\x98\xee\x00\xff\x90\xee\xff\xfe\x87\xee\x05\xff\x7f\xee\n\xffz\xee\x0b\xffw\xee\x07\xffs\xee\x07\xffk\xee\x02\xffc\xee\xf6\xfe[\xee\xf2\xfeV\xee\xf4\xfeO\xee\xfc\xfeI\xee\x06\xffC\xee\n\xff;\xee\x07\xff3\xee\xff\xfe0\xee\xf5\xfe)\xee\xf2\xfe"\xee\xf1\xfe\x1c\xee\xf7\xfe\x14\xee\x05\xff\x0c\xee\x12\xff\x08\xee\x12\xff\x02\xee\x07\xff\xfd\xed\xfa\xfe\xf6\xed\xf6\xfe\xee\xed\xf7\xfe\xe7\xed\xfb\xfe\xe0\xed\xf8\xfe\xd9\xed\xf4\xfe\xd7\xed\xf9\xfe\xd2\xed\x03\xff\xcb\xed\x02\xff\xc4\xed\xfb\xfe\xbc\xed\xf8\xfe\xb5\xed\x02\xff\xad\xed\x07\xff\xa7\xed\x08\xff\xa3\xed\n\xff\x9d\xed\x10\xff\x96\xed\x12\xff', b'\x8e\xed\x0f\xff\x89\xed\t\xff\x82\xed\x07\xff\x7f\xed\x07\xff{\xed\x0c\xffu\xed\r\xffn\xed\x06\xffg\xed\xfb\xfe`\xed\xf5\xfeX\xed\xf8\xfeN\xed\xfd\xfeL\xed\x00\xffG\xed\x02\xffD\xed\x03\xff?\xed\x03\xff8\xed\xfe\xfe1\xed\xf5\xfe+\xed\xf1\xfe%\xed\xf3\xfe\x1f\xed\xf7\xfe\x19\xed\xfd\xfe\x15\xed\x0c\xff\x10\xed\x1a\xff\x0b\xed#\xff\x05\xed#\xff\xff\xec\x1a\xff\xf8\xec\x0c\xff\xf4\xec\x00\xff\xee\xec\xf8\xfe\xe9\xec\xf7\xfe\xe3\xec\xfd\xfe\xdf\xec\x02\xff\xd8\xec\x03\xff\xd3\xec\x07\xff\xce\xec\x05\xff\xc6\xec\x01\xff\xc0\xec\xfb\xfe\xbb\xec\xfb\xfe\xb8\xec\x02\xff\xb1\xec\x04\xff\xad\xec\xfd\xfe\xa8\xec\xf4\xfe\xa1\xec\xec\xfe\x9d\xec\xef\xfe\x98\xec\xf6\xfe\x91\xec\x01\xff\x8b\xec\x08\xff\x88\xec\x0e', b'\xff\x82\xec\x13\xffz\xec\x16\xffu\xec\x18\xffn\xec\x0f\xffk\xec\x01\xffh\xec\xf7\xfea\xec\xf8\xfe^\xec\xfe\xfe[\xec\x05\xffV\xec\t\xffN\xec\x0c\xffJ\xec\x10\xffC\xec\x10\xff>\xec\x04\xff8\xec\xfa\xfe2\xec\xf5\xfe-\xec\xf7\xfe\'\xec\xfa\xfe"\xec\xfe\xfe\x1d\xec\x04\xff\x1a\xec\x11\xff\x14\xec\x14\xff\x0f\xec\x08\xff\n\xec\xf8\xfe\x05\xec\xef\xfe\xfe\xeb\xf0\xfe\xfb\xeb\xfa\xfe\xf8\xeb\xff\xfe\xf5\xeb\x00\xff\xf0\xeb\x01\xff\xeb\xeb\x03\xff\xe7\xeb\x02\xff\xe1\xeb\xfe\xfe\xdd\xeb\xfa\xfe\xd7\xeb\xfa\xfe\xd3\xeb\xfe\xfe\xce\xeb\x05\xff\xcd\xeb\x08\xff\xc5\xeb\n\xff\xc1\xeb\r\xff\xbc\xeb\x13\xff\xb7\xeb\x0e\xff\xb1\xeb\x06\xff\xaf\xeb\x04\xff\xa7\xeb\x02\xff\xa4\xeb\xff\xfe\xa0\xeb\xfd\xfe\x9a\xeb', b'\xfd\xfe\x96\xeb\xff\xfe\x93\xeb\x00\xff\x8d\xeb\x04\xff\x88\xeb\x03\xff\x85\xeb\x00\xff~\xeb\x08\xffy\xeb\x1a\xffu\xeb\'\xffp\xeb\'\xffn\xeb\x1f\xffk\xeb\x1a\xfff\xeb\x14\xffb\xeb\x13\xff\\\xeb\x0e\xffV\xeb\x06\xffT\xeb\x00\xffR\xeb\xf8\xfeK\xeb\xf0\xfeD\xeb\xea\xfe@\xeb\xe8\xfe>\xeb\xee\xfe7\xeb\xf5\xfe3\xeb\xfa\xfe1\xeb\xfe\xfe/\xeb\xfb\xfe)\xeb\xf6\xfe"\xeb\xfb\xfe \xeb\x01\xff\x1d\xeb\n\xff\x19\xeb\x10\xff\x13\xeb\x12\xff\x11\xeb\x17\xff\r\xeb\x1e\xff\x07\xeb\x1d\xff\x02\xeb\x19\xff\xfd\xea\x14\xff\xfa\xea\x0b\xff\xfa\xea\xfd\xfe\xf5\xea\xf0\xfe\xef\xea\xe7\xfe\xe9\xea\xea\xfe\xe5\xea\xf1\xfe\xe3\xea\xf7\xfe\xde\xea\x00\xff\xdc\xea\r\xff\xd7\xea\x12\xff\xd5\xea\x05\xff\xcd', b"\xea\xf8\xfe\xca\xea\xf5\xfe\xc9\xea\xf8\xfe\xc6\xea\xff\xfe\xbf\xea\x00\xff\xba\xea\xf9\xfe\xb5\xea\xf3\xfe\xb1\xea\xf1\xfe\xaf\xea\xf0\xfe\xab\xea\xf3\xfe\xa6\xea\xfc\xfe\xa1\xea\x06\xff\x9f\xea\r\xff\x9b\xea\x10\xff\x98\xea\x10\xff\x96\xea\x0f\xff\x93\xea\r\xff\x8f\xea\x07\xff\x8b\xea\x01\xff\x86\xea\x04\xff\x80\xea\x06\xff|\xea\x03\xffz\xea\xfa\xfew\xea\xf4\xfet\xea\xf6\xfeo\xea\xfc\xfel\xea\xfe\xfef\xea\xfd\xfea\xea\xfd\xfe_\xea\x03\xff[\xea\x0c\xffY\xea\x0e\xffV\xea\x08\xffV\xea\xff\xfeS\xea\xfb\xfeN\xea\xfd\xfeJ\xea\xff\xfeE\xea\xfa\xfe?\xea\xf5\xfe>\xea\xf9\xfe;\xea\x03\xff8\xea\x0b\xff4\xea\x10\xff1\xea\x0e\xff-\xea\x07\xff'\xea\xff\xfe#\xea\xfb\xfe\x1e\xea\x03\xff"]`

## StringsIndexed

> This object provides easy access to strings which are scattered around     the header files. The StringsSection contains strings, but various headers     contain values which point to a certain string index. This class connects     the two, and provides direct access to those strings by their indexed name. 

* lADCChannelName = `['IN 0', 'IN 1']`
* lADCUnits = `['pA', 'A']`
* lDACChannelName = `['Cmd 0', 'Cmd 1', 'Cmd 2', 'Cmd 3', 'AO #4', 'AO #5', 'AO #6', 'AO #7']`
* lDACChannelUnits = `['mV', 'mV', 'mV', 'mV', 'mV', 'mV', 'mV', 'mV']`
* lDACFilePath = `['', '', '', '', '', '', '', '']`
* lFileComment = ``
* nLeakSubtractADC = `['', '', '', '', '', '', '', '']`
* uCreatorName = `Clampex`
* uModifierName = ``
* uProtocolPath = `\\Spike\locked\Protocols\permanent\0201 memtest.pro`