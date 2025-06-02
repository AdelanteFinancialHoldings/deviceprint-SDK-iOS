Pod::Spec.new do |s|
  s.name         = 'AddiMobile-FraudForce'
  s.version      = '5.7.0'
  s.summary      = 'TransUnion TruValidate Device Risk SDK for iOS (formerly FraudForce)'
  s.description  = <<-DESC
    Device Risk SDK for iOS, formerly known as FraudForce, provides device-based risk detection for fraud and identity solutions. It inspects the device and generates a blackbox for risk assessment. Integrates with native and hybrid apps.
  DESC
  s.homepage     = 'https://github.com/AdelanteFinancialHoldings/deviceprint-SDK-iOS'
  s.license      = { :type => 'Commercial', :file => 'LICENSE.txt' }
  s.author       = { 'iovation, a TransUnion company' => 'support@iovation.com' }
  s.platform     = :ios, '15.0'
  s.source       = { :git => 'https://github.com/AdelanteFinancialHoldings/deviceprint-SDK-iOS.git', :branch => 'master' }
  s.vendored_frameworks = 'FraudForce.xcframework'
  s.frameworks   = ['CoreTelephony', 'Security', 'SystemConfiguration']
  s.weak_frameworks = ['AdSupport', 'CoreLocation']
  s.pod_target_xcconfig = {
    'OTHER_LDFLAGS' => '-ObjC'
  }
  s.requires_arc = true
  s.module_name  = 'FraudForce'
  s.documentation_url = 'https://github.com/AdelanteFinancialHoldings/deviceprint-SDK-iOS'
end
